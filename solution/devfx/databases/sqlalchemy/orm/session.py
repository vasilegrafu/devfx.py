import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm
import sqlalchemy.inspection
import devfx.core as core
import devfx.exceptions as excps
import devfx.diagnostics as dgn

"""------------------------------------------------------------------------------------------------
"""
class Session(object):
    def __init__(self, database_url, echo=False, autoflush=False, autocommit=False, expire_on_commit=True, isolation_level=None):
        """

        :param database_url:
        :param echo:
        :param autoflush:
        :param autocommit:
        :param expire_on_commit:
        :param isolation_level: Possible values: None, "SERIALIZABLE", "REPEATABLE_READ", "READ_COMMITTED", "READ_UNCOMMITTED" and "AUTOCOMMIT"
        """

        self.__database_url = database_url
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
    def database_url(self):
        return self.__database_url

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
                engine = sa.create_engine(self.__database_url, echo=self.__echo)
            else:
                engine = sa.create_engine(self.__database_url, echo=self.__echo, isolation_level=self.__isolation_level)
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
    # def save_data(self, entity, data):
    #     columns = {column.name: column for column in sa.inspection.inspect(entity).c}
    #     primary_key_columns = {column.name: column for column in sa.inspection.inspect(entity).primary_key}
    #     instances = []
    #     for row in data.itertuples():
    #         instance = self.__session.query(entity) \
    #                                  .get([core.getattr(row, column_name) for column_name in primary_key_columns])
    #         if(instance is None):
    #             instance = entity()                   
    #             for column_name in columns:
    #                 core.setattr(instance, column_name, core.getattr(row, column_name))
    #             instances.append(instance)
    #         else:
    #             for column_name in columns:
    #                 core.setattr(instance, column_name, core.getattr(row, column_name))
    #     self.__session.bulk_save_objects(instances)

    # def save_data(self, entity, data):
    #     columns = [column for column in sa.inspection.inspect(entity).c]
    #     primary_key_columns = [column for column in sa.inspection.inspect(entity).primary_key]
    #     instances = []
    #     data_chunk_size = 100
    #     data_chunks = [data[i:i+data_chunk_size].copy() for i in range(0, data.shape[0], data_chunk_size)]
    #     for data_chunk in data_chunks:
    #         data_chunk['pk_tuple'] = data_chunk[[column.name for column in primary_key_columns]].apply(tuple, axis=1)

    #         instances_from_db = self.__session.query(entity) \
    #                                           .filter(sa.or_(*[sa.and_(*[column == core.getattr(data_chunk_row, column.name) for column in primary_key_columns]) for data_chunk_row in data_chunk.itertuples()])) \
    #                                           .all()  
    #         instances_from_db = {tuple([core.getattr(instance, column.name) for column in primary_key_columns]): instance for instance in instances_from_db}
            
    #         for data_chunk_row in data_chunk.itertuples(index=None, name=None):
    #             pk_tuple = data_chunk_row[data_chunk.columns.get_loc('pk_tuple')]
    #             if(pk_tuple not in instances_from_db):
    #                 instance = entity()   
    #             else:
    #                 instance = instances_from_db[pk_tuple]
    #             for column in columns:
    #                 core.setattr(instance, column.name, data_chunk_row[data_chunk.columns.get_loc(column.name)])
    #             instances.append(instance)
    #     self.__session.bulk_save_objects(instances)
    
    def save_data(self, entity, data):
        primary_key_columns = [column for column in sa.inspection.inspect(entity).primary_key]
        instances = []
        data_chunk_size = 100
        data_chunks = [data[i:i+data_chunk_size].copy() for i in range(0, data.shape[0], data_chunk_size)]
        for data_chunk in data_chunks:
            data_chunk.set_index([column.name for column in primary_key_columns], inplace=True)
            if(len(primary_key_columns) == 1):
                instances_from_db = self.__session.query(entity) \
                                                  .filter(sa.or_(*[primary_key_columns[0] == data_chunk_row[0] for data_chunk_row in data_chunk.itertuples()])) \
                                                  .all() 
                instances_from_db = {core.getattr(instance, primary_key_columns[0].name): instance for instance in instances_from_db} 
            elif(len(primary_key_columns) > 1):
                instances_from_db = self.__session.query(entity) \
                                                  .filter(sa.or_(*[sa.and_(*[column == data_chunk_row[0][i] for i, column in enumerate(primary_key_columns)]) for data_chunk_row in data_chunk.itertuples()])) \
                                                  .all()  
                instances_from_db = {tuple([core.getattr(instance, column.name) for column in primary_key_columns]): instance for instance in instances_from_db}
            else:
                raise excps.NotSupportedError()                             
            
            for data_chunk_row in data_chunk.itertuples():
                if(data_chunk_row[0] not in instances_from_db):
                    instance = entity() 
                    if(len(data_chunk.index.names) == 1):
                        core.setattr(instance, data_chunk.index.names[0], data_chunk_row[0])
                    elif(len(data_chunk.index.names) > 1):
                        for (i, _) in enumerate(data_chunk.index.names):
                            core.setattr(instance, data_chunk.index.names[i], data_chunk_row[0][i])
                    else:
                        raise excps.NotSupportedError()  
                else:
                    instance = instances_from_db[data_chunk_row[0]]

                for (i, column) in enumerate(data_chunk.columns.to_list()):
                    core.setattr(instance, column, core.getattr(data_chunk_row, column))
                instances.append(instance)
                
        self.__session.bulk_save_objects(instances)

    def remove_data(self, entity, data):
        primary_key_columns = [column for column in sa.inspection.inspect(entity).primary_key]
        instances = []
        for data_row in data.itertuples():
            instance = self.__session.query(entity) \
                                     .get([core.getattr(data_row, column.name) for column in primary_key_columns])
            if(instance is None):
                pass
            else:
                self.__session.delete(instance)

    def query_data(self, columns, index=None):
        return Session.__QueryData(columns=columns, index=index, session=self.__session)

    class __QueryData(object):
        def __init__(self, columns, index, session):
            self.__columns = columns if (core.is_iterable(columns)) else [columns]
            self.__index = index
            self.__session = session

            self.__query = self.__session.query(*self.__columns)
            
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
            if(core.is_instance(self.__columns[0], sa.ext.declarative.api.DeclarativeMeta)):
                data = pd.DataFrame.from_records(data=[instance.__dict__ for instance in instances], 
                                                 columns=[column.name for column in sa.inspection.inspect(*self.__columns).c])
                if(self.__index is not None):
                    data.set_index([column.name for column in self.__index], inplace=True)
                return data
            elif(core.is_instance(self.__columns[0], sa.orm.attributes.InstrumentedAttribute)):
                data = pd.DataFrame.from_records(data=[instance for instance in instances], 
                                                 columns=[column.name for column in self.__columns])
                if(self.__index is not None):
                    data.set_index([column.name for column in self.__index], inplace=True)
                return data
            else:
                raise excps.NotSupportedError()

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