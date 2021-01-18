import devfx.databases.sqlalchemy as sa

class Session(sa.orm.Session):
    def __init__(self, config, expire_on_commit=True, isolation_level=None):
        super().__init__(url=config.database.url, expire_on_commit=expire_on_commit)