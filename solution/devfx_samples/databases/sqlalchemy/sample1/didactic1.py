import devfx.databases.sqlalchemy as sa

""" Schema
"""
database_metadata = sa.create_database_metadata()

entity1 = sa.Table('entity1', database_metadata,
                     sa.Column_as__id(sa.types.Integer(), autoincrement=True),

                     sa.Column_as__created_on(),
                     sa.Column_as__updated_on())

entity2 = sa.Table('entity2', database_metadata,
                     sa.Column_as__id(sa.types.Integer(), autoincrement=True),
                     sa.Column_as_ForeignKey('id_entity1', 'entity1.id'),

                     sa.Column_as_BigInteger('BigInteger'),
                     sa.Column_as_Integer('Integer'),
                     sa.Column_as_SmallInteger('SmallInteger'),
                     sa.Column_as_FixedPointNumber('FixedPointNumber'),
                     sa.Column_as_FloatingPointNumber('FloatingPointNumber'),
                     sa.Column_as_String('String'),
                     sa.Column_as_Text('Text'),
                     sa.Column_as_Boolean('Boolean'),
                     sa.Column_as_Date('Date'),
                     sa.Column_as_DateTime('DateTime'),
                     sa.Column_as_Time('Time'),
                     sa.Column_as_Timedelta('Timedelta'),

                     sa.Column_as__created_on(),
                     sa.Column_as__updated_on())

""" Connection string
"""
connection_string = 'sqlite:///devfx_samples/databases/sqlalchemy/sample1/didactic1.db'

""" Deploy
"""
sa.deploy_database_metadata(database_metadata=database_metadata, connection_string=connection_string)

""" Create
"""
with sa.DatabaseConnection(connection_string) as dbconnection:
    entity1_insert_result = dbconnection.execute(entity1.insert())
    print(entity1_insert_result)

""" Query
"""
with sa.DatabaseConnection(connection_string) as dbconnection:
    entity1_select_result = dbconnection.execute(entity1.select()).fetchall()
    print(entity1_select_result)


