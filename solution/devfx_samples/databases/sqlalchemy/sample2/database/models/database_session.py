import devfx.databases.sqlalchemy as sa

class DatabaseSession(sa.orm.DatabaseSession):
    def __init__(self, config, expire_on_commit=True, isolation_level=None):
        super().__init__(connection_string=config.database.connection_string, expire_on_commit=expire_on_commit)