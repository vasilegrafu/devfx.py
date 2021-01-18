import sqlalchemy as sa
import sqlalchemy.orm

"""------------------------------------------------------------------------------------------------
"""
class Session(object):
    def __init__(self, url, echo=False, autoflush=True, autocommit=False, expire_on_commit=True, isolation_level=None):
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

        self.__sesssion = None

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
        if(self.__sesssion is None):
            if(self.__isolation_level is None):
                engine = sa.create_engine(self.__url, echo=self.__echo)
            else:
                engine = sa.create_engine(self.__url, echo=self.__echo, isolation_level=self.__isolation_level)
            Session = sa.orm.sessionmaker(bind=engine, autoflush=self.__autoflush, autocommit=self.__autocommit, expire_on_commit=self.__expire_on_commit)
            self.__sesssion = Session()

    @property
    def bind(self):
        return self.__sesssion.bind

    def begin(self):
        return self.__sesssion.begin()

    def flush(self, instances=None):
        self.__sesssion.flush(objects=instances)

    def rollback(self):
        self.__sesssion.rollback()

    def commit(self):
        self.__sesssion.commit()

    def close(self):
        self.__sesssion.close()
        self.__sesssion = None

    """----------------------------------------------------------------
    """
    def execute(self, statement, params=None):
        return self.__sesssion.execute(statement, params=params)

    # ----------------------------------------------------------------
    def add(self, instance):
        self.__sesssion.add(instance)

    def add_all(self, instances):
        self.__sesssion.add_all(instances)


    # ----------------------------------------------------------------
    def bulk_save(self, instances):
        self.__sesssion.bulk_save_objects(instances)

    # ----------------------------------------------------------------
    def expire(self, instance, attribute_names=None):
        self.__sesssion.expire(instance, attribute_names=attribute_names)

    def expire_all(self, instances, attribute_names=None):
        for instance in instances:
            self.expire(instance, attribute_names=attribute_names)


    def refresh(self, instance, attribute_names=None):
        self.__sesssion.refresh(instance, attribute_names=attribute_names)

    def refresh_all(self, instances, attribute_names=None):
        for instance in instances:
            self.expire(instance, attribute_names=attribute_names)

    # ----------------------------------------------------------------
    def expunge(self, instance):
        self.__sesssion.expunge(instance)

    def expunge_all(self, instances):
        for instance in instances:
            self.expunge(instance)

    # ----------------------------------------------------------------
    def delete(self, instance):
        self.__sesssion.delete(instance)

    def delete_all(self, instances):
        for instance in instances:
            self.delete(instance)

    """----------------------------------------------------------------
    """
    def is_modified(self, instance, include_collections=True):
        return self.__sesssion.is_modified(instance, include_collections=include_collections)

    """----------------------------------------------------------------
    """
    def query(self, *entities, **kwargs):
        return self.__sesssion.query(*entities, **kwargs)


    """----------------------------------------------------------------
    """
    def data_append(self, entity, data, index=False, index_label=None, chunksize=256):
        data.to_sql(name=entity.__tablename__, con=self.__session.bind, if_exists='append', index=index, index_label=index_label, chunksize=chunksize)

    def data_remove(self, query=None):
        pass

    def data_get(self, query=None):
        pass