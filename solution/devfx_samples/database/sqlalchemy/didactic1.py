import devfx.databases.sqlalchemy as sadb

""" Schema
"""
database_metadata = sadb.create_database_metadata()

entity1 = sadb.Table('entity1', database_metadata,
                     sadb.Column_as__id(sadb.types.Integer(), autoincrement=True),

                     sadb.Column_as__created_on(),
                     sadb.Column_as__updated_on())

entity2 = sadb.Table('entity2', database_metadata,
                     sadb.Column_as__id(sadb.types.Integer(), autoincrement=True),
                     sadb.Column_as_ForeignKey('id_entity1', 'entity1.id'),

                     sadb.Column_as_BigInteger('BigInteger'),
                     sadb.Column_as_Integer('Integer'),
                     sadb.Column_as_SmallInteger('SmallInteger'),
                     sadb.Column_as_FixedPointNumber('FixedPointNumber'),
                     sadb.Column_as_FloatingPointNumber('FloatingPointNumber'),
                     sadb.Column_as_String('String'),
                     sadb.Column_as_Text('Text'),
                     sadb.Column_as_Boolean('Boolean'),
                     sadb.Column_as_Date('Date'),
                     sadb.Column_as_DateTime('DateTime'),
                     sadb.Column_as_Time('Time'),
                     sadb.Column_as_Timedelta('Timedelta'),

                     sadb.Column_as__created_on(),
                     sadb.Column_as__updated_on())

""" Connection string
"""
connection_string = 'sqlite:///devfx_samples/database/sqlalchemy/didactic1.db'

""" Deploy
"""
sadb.deploy_database_metadata(database_metadata=database_metadata, connection_string=connection_string)

""" Create
"""
with sadb.Connection(connection_string) as connection:
    entity1_insert_result = connection.execute(entity1.insert())
    print(entity1_insert_result)

""" Query
"""
with sadb.Connection(connection_string) as connection:
    entity1_select_result = connection.execute(entity1.select()).fetchall()
    print(entity1_select_result)


