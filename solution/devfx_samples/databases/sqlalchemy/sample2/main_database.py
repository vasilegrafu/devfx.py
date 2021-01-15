import datetime as dt
from devfx_samples.databases.sqlalchemy.sample2 import database as db
from devfx_samples.databases.sqlalchemy.sample2 import configuration as config

"""------------------------------------------------------------------------------------------------
"""
if __name__ == "__main__":
    db.DatabaseMetadataDeployer.deploy(config)

