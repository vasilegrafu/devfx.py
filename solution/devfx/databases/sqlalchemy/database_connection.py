import sqlalchemy as sa

"""------------------------------------------------------------------------------------------------
"""
class DatabaseConnection(object):
    def __init__(self, connection_string, echo=False, isolation_level=None):
        """

        :param connection_string:
        :param echo:
        :param isolation_level: Possible values: None, "SERIALIZABLE", "REPEATABLE_READ", "READ_COMMITTED", "READ_UNCOMMITTED" and "AUTOCOMMIT"
        """

        self.__connection_string = connection_string
        self.__echo = echo
        self.__isolation_level = isolation_level

        self.__connection = None

    """----------------------------------------------------------------
    """
    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        if(exception_type is None):
            self.close()
        else:
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
    def isolation_level(self):
        return self.__isolation_level

    """----------------------------------------------------------------
    """
    def connect(self):
        if(self.__connection is None):
            if(self.__isolation_level is None):
                engine = sa.create_engine(self.__connection_string, echo=self.__echo)
            else:
                engine = sa.create_engine(self.__connection_string, echo=self.__echo, isolation_level=self.__isolation_level)
            self.__connection = engine.connect()

    def close(self):
        self.__connection.close()
        self.__connection = None

    """----------------------------------------------------------------
    """
    def execute(self, statement, *params, **kwparams):
        return self.__connection.execute(statement, multiparams=params, params=kwparams)

