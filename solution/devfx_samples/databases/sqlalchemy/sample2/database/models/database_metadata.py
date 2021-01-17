import devfx.databases.sqlalchemy as sa

BaseDatabaseEntity = sa.orm.create_base_database_entity_type()

class DatabaseMetadataDeployer(object):
    @staticmethod
    def deploy(configuration):
        sa.orm.deploy_database_metadata(base_database_entity_type=BaseDatabaseEntity, connection_string=configuration.database.connection_string)

