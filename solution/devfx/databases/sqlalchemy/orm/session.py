import sqlalchemy as sa
import sqlalchemy.orm

"""------------------------------------------------------------------------------------------------
"""
class Session(object):
    def __init__(self, connection_string, echo=False, autoflush=True, autocommit=False, expire_on_commit=True, isolation_level=None):
        """

        :param connection_string:
        :param echo:
        :param autoflush:
        :param autocommit:
        :param expire_on_commit:
        :param isolation_level: Possible values: None, "SERIALIZABLE", "REPEATABLE_READ", "READ_COMMITTED", "READ_UNCOMMITTED" and "AUTOCOMMIT"
        """

        self.__connection_string = connection_string
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
    def connection_string(self):
        return self.__connection_string

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
                engine = sa.create_engine(self.__connection_string, echo=self.__echo)
            else:
                engine = sa.create_engine(self.__connection_string, echo=self.__echo, isolation_level=self.__isolation_level)
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

    """----------------------------------------------------------------
    """
    def execute(self, statement, params=None):
        return self.__session.execute(statement, params=params)

    # ----------------------------------------------------------------
    def add(self, instance):
        self.__session.add(instance)

    def add_all(self, instances):
        for instance in instances:
            self.add(instance)

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
