import devfx.databases.sqlalchemy as sa
from .models.database_metadata import BaseDatabaseEntity

"""------------------------------------------------------------------------------------------------
"""
class DatabaseMetadataDeployer(object):
    @staticmethod
    def deploy(configuration):
        sa.orm.deploy_database_metadata(base_database_entity_type=BaseDatabaseEntity, connection_string=configuration.database.connection_string)
