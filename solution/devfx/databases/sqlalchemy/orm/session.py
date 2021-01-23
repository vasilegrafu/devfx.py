import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm
import sqlalchemy.inspection
import devfx.core as core
import devfx.diagnostics as dgn

"""------------------------------------------------------------------------------------------------
"""
class Session(object):
    def __init__(self, url, echo=False, autoflush=False, autocommit=False, expire_on_commit=True, isolation_level=None):
        """

        :param url:
        :param echo:
        :param autoflush:
        :param autocommit:
        :param expire_on_commit:
        :param isolation_level: Possible values: None, "SERIALIZABLE", "REPEATABLE_READ", "READ_COMMITTED", "READ_UNCOMMITTED" and "AUTOCOMMIT"
        """

        self.__url = url
        self.__echo = echo
        self.__autoflush = autoflush
        self.__autocommit = autocommit
        self.__expire_on_commit = expire_on_commit
        self.__isolation_level = isolation_level

        self.__session = None

    """----------------------------------------------------------------
    """
    def __enter__(self):
        self.open()
        if(self.__autocommit==True):
            self.begin()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if(exception_type is None):
            self.commit()
            self.close()
        else:
            self.rollback()
            self.close()
            raise exception_value

    """----------------------------------------------------------------
    """
    @property
    def url(self):
        return self.__url

    @property
    def echo(self):
        return self.__echo

    @property
    def autoflush(self):
        return self.__autoflush

    @property
    def autocommit(self):
        return self.__autocommit

    @property
    def expire_on_commit(self):
        return self.__expire_on_commit

    @property
    def isolation_level(self):
        return self.__isolation_level

    """----------------------------------------------------------------
    """
    def open(self):
        if(self.__session is None):
            if(self.__isolation_level is None):
                engine = sa.create_engine(self.__url, echo=self.__echo)
            else:
                engine = sa.create_engine(self.__url, echo=self.__echo, isolation_level=self.__isolation_level)
            Session = sa.orm.sessionmaker(bind=engine, autoflush=self.__autoflush, autocommit=self.__autocommit, expire_on_commit=self.__expire_on_commit)
            self.__session = Session()

    @property
    def bind(self):
        return self.__session.bind

    def begin(self):
        return self.__session.begin()

    def flush(self, instances=None):
        self.__session.flush(objects=instances)

    def rollback(self):
        self.__session.rollback()

    def commit(self):
        self.__session.commit()

    def close(self):
        self.__session.close()
        self.__session = None

    """----------------------------------------------------------------
    """
    def execute(self, statement, params=None):
        return self.__session.execute(statement, params=params)

    # ----------------------------------------------------------------
    def add(self, instance):
        self.__session.add(instance)

    def add_all(self, instances):
        self.__session.add_all(instances)


    # ----------------------------------------------------------------
    def bulk_save(self, instances):
        self.__session.bulk_save_objects(instances)

    # ----------------------------------------------------------------
    def expire(self, instance, attribute_names=None):
        self.__session.expire(instance, attribute_names=attribute_names)

    def expire_all(self, instances, attribute_names=None):
        for instance in instances:
            self.expire(instance, attribute_names=attribute_names)


    def refresh(self, instance, attribute_names=None):
        self.__session.refresh(instance, attribute_names=attribute_names)

    def refresh_all(self, instances, attribute_names=None):
        for instance in instances:
            self.expire(instance, attribute_names=attribute_names)

    # ----------------------------------------------------------------
    def expunge(self, instance):
        self.__session.expunge(instance)

    def expunge_all(self, instances):
        for instance in instances:
            self.expunge(instance)

    # ----------------------------------------------------------------
    def delete(self, instance):
        self.__session.delete(instance)

    def delete_all(self, instances):
        for instance in instances:
            self.delete(instance)

    """----------------------------------------------------------------
    """
    def is_modified(self, instance, include_collections=True):
        return self.__session.is_modified(instance, include_collections=include_collections)

    """----------------------------------------------------------------
    """
    def query(self, *entities, **kwargs):
        return self.__session.query(*entities, **kwargs)


    """----------------------------------------------------------------
    """
    instances = []
    def save_data(self, entity_type, data):
        columns = {column.name: column for column in sa.inspection.inspect(entity_type).c}
        pkcolumns = {column.name: column for column in sa.inspection.inspect(entity_type).primary_key}
        non_pkcolumns = {name: columns[name] for name in set(columns) - set(pkcolumns)}
        for index, row in data.iterrows():
            index = [index] if (data.index.nlevels == 1) else index
            query = self.__session.query(entity_type)
            query = query.filter(sa.and_(*[pkcolumns[column_name] == index[data.index.names.index(column_name)] for column_name in pkcolumns]))
            instance = query.one_or_none()
            if(instance is None):
                instance = entity_type()                   
                for column_name in pkcolumns:
                    core.setattr(instance, column_name, index[data.index.names.index(column_name)])
                for column_name in non_pkcolumns:
                    core.setattr(instance, column_name, row[column_name])
                self.__session.add(instance)
            else:
                for column_name in pkcolumns:
                    core.setattr(instance, column_name, index[data.index.names.index(column_name)])
                for column_name in non_pkcolumns:
                    core.setattr(instance, column_name, row[column_name])
                  
    def remove_data(self, entity_type, data):
        columns = {column.name: column for column in sa.inspection.inspect(entity_type).c}
        pkcolumns = {column.name: column for column in sa.inspection.inspect(entity_type).primary_key}
        non_pkcolumns = {name: columns[name] for name in set(columns) - set(pkcolumns)}
        for index, row in data.iterrows():
            index = [index] if (data.index.nlevels == 1) else index
            query = self.__session.query(entity_type)
            query = query.filter(sa.and_(*[pkcolumns[column_name] == index[data.index.names.index(column_name)] for column_name in pkcolumns]))
            instance = query.one_or_none()
            if(instance is None):
                pass
            else:
                self.__session.delete(instance)

    def get_data(self, entity_type, where=None, order_by=None, limit=None):
        query = self.__session.query(entity_type)
        if(where is not None):
            query = query.filter(where(entity_type))
        if(order_by is not None):
            query = query.order_by(order_by(entity_type))
        if(limit is not None):
            query = query.limit(limit)
        instances = query.all()
        data = pd.DataFrame.from_records(data=[instance.__dict__ for instance in instances], 
                                         columns=[column.name for column in sa.inspection.inspect(entity_type).c])
        data.set_index([column.name for column in sa.inspection.inspect(entity_type).primary_key], inplace=True)
        return data

    def get_data_count(self, entity_type, where=None, limit=None):
        query = self.__session.query(entity_type)
        if(where is not None):
            query = query.filter(where(entity_type))
        if(limit is not None):
            query = query.limit(limit)
        data_count = query.count()
        return data_count
