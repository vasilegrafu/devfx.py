import devfx.databases.sqlalchemy as sa

BaseEntity = sa.orm.create_base_entity_type()

class MetadataDeployer(object):
    @staticmethod
    def deploy(configuration):
        sa.orm.deploy_metadata(base_entity_type=BaseEntity, url=configuration.database.url)

