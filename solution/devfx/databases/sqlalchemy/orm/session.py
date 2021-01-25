import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm
import sqlalchemy.inspection
import devfx.core as core
import devfx.exceptions as excs
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

    @property
    def is_active(self):
        return self.__session is None

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

    def is_modified(self, instance, include_collections=True):
        return self.__session.is_modified(instance, include_collections=include_collections)

    """----------------------------------------------------------------
    """
    def execute(self, statement, params=None):
        return self.__session.execute(statement, params=params)

    # ----------------------------------------------------------------
    def save_bulk(self, instances):
        self.__session.bulk_save_objects(instances)

    # ----------------------------------------------------------------
    def add(self, instance):
        self.__session.add(instance)

    def add_all(self, instances):
        self.__session.add_all(instances)

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
    def query(self, *entities):
        return Session.__Query(entities=entities, session=self.__session)

    class __Query(sa.orm.Query):
        def __init__(self, entities, session=None):
                super().__init__(entities, session=session)

    def first(self):
        instance = self.first()
        if(instance is None):
            raise sa.orm.exc.NoResultFound()
        return instance

    def first_or_none(self):
        instance = self.first()
        if(instance is None):
            return None
        return instance

    """----------------------------------------------------------------
    """
    instances = []
    def save_data(self, entity, data):
        columns = {column.name: column for column in sa.inspection.inspect(entity).c}
        primary_key_columns = {column.name: column for column in sa.inspection.inspect(entity).primary_key}
        instances = []
        for row in data.itertuples():
            instance = self.__session.query(entity) \
                                     .get([core.getattr(row, column_name) for column_name in primary_key_columns])
            if(instance is None):
                instance = entity()                   
                for column_name in columns:
                    core.setattr(instance, column_name, core.getattr(row, column_name))
                instances.append(instance)
            else:
                for column_name in columns:
                    core.setattr(instance, column_name, core.getattr(row, column_name))
        self.__session.bulk_save_objects(instances)
                  
    def remove_data(self, entity, data):
        columns = {column.name: column for column in sa.inspection.inspect(entity).c}
        primary_key_columns = {column.name: column for column in sa.inspection.inspect(entity).primary_key}
        instances = []
        for row in data.itertuples():
            instance = self.__session.query(entity) \
                                     .get([core.getattr(row, column_name) for column_name in primary_key_columns])
            if(instance is None):
                pass
            else:
                self.__session.delete(instance)

    def query_data(self, *entities):
        return Session.__QueryData(entities=entities, session=self.__session)

    class __QueryData(object):
        def __init__(self, entities, session):
            self.__entities = entities
            self.__session = session

            self.__query = self.__session.query(*entities)
            
        def filter(self, criterion):
            self.__query = self.__query.filter(criterion)
            return self

        def order_by(self, criterion):
            self.__query = self.__query.order_by(criterion)
            return self

        def limit(self, limit):
            self.__query = self.__query.limit(limit)
            return self

        def count(self):
            count = self.__query.count()
            return count

        def __get_data(self, instances):
            if(len(self.__entities) == 0):
                raise excs.NotSupportedError()
            elif(len(self.__entities) == 1):
                data = pd.DataFrame.from_records(data=[instance.__dict__ for instance in instances], 
                                                 columns=[column.name for column in sa.inspection.inspect(*self.__entities).c])
                return data
            else:
                data = pd.DataFrame.from_records(data=[instance for instance in instances], 
                                                 columns=[column.name for column in self.__entities])
                return data

        def all(self):
            instances = self.__query.all()
            data = self.__get_data(instances)
            return data

        def one(self):
            instance = self.__query.one()
            instances = [instance]
            data = self.__get_data(instances)
            return data

        def one_or_none(self):
            instance = self.__query.one_or_none()
            if(instance is None):
                return None
            instances = [instance]
            data = self.__get_data(instances)
            return data

        def first(self):
            instance = self.__query.first()
            if(instance is None):
                raise sa.orm.exc.NoResultFound()
            instances = [instance]
            data = self.__get_data(instances)
            return data

        def first_or_none(self):
            instance = self.__query.first()
            if(instance is None):
                return None
            instances = [instance]
            data = self.__get_data(instances)
            return data