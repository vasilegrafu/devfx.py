import devfx.databases.sqlalchemy as db

""" Schema
"""
database_metadata = db.create_database_metadata()

entity1 = db.Table('entity1', database_metadata,
                    db.Column_as__id(),

                    db.Column_as__created_on(),
                    db.Column_as__updated_on())

entity2 = db.Table('entity2', database_metadata,
                    db.Column_as__id(),
                    db.Column_as_ForeignKey('id_entity1', 'entity1.id'),

                    db.Column_as_BigInteger('BigInteger'),
                    db.Column_as_Integer('Integer'),
                    db.Column_as_SmallInteger('SmallInteger'),
                    db.Column_as_FixedPointNumber('FixedPointNumber'),
                    db.Column_as_FloatingPointNumber('FloatingPointNumber'),
                    db.Column_as_String('String'),
                    db.Column_as_UnicodeString('UnicodeString'),
                    db.Column_as_Text('Text'),
                    db.Column_as_UnicodeText('UnicodeText'),
                    db.Column_as_Boolean('Boolean'),
                    db.Column_as_Date('Date'),
                    db.Column_as_DateTime('DateTime'),
                    db.Column_as_Time('Time'),
                    db.Column_as_Timedelta('Timedelta'),

                    db.Column_as__created_on(),
                    db.Column_as__updated_on())

""" Connection string
"""
connection_string = 'sqlite:///core.db'

""" Deploy
"""
db.deploy_database_schema(database_metadata=database_metadata, connection_string=connection_string)

""" Create
"""
with db.Connection(connection_string) as connection:
    entity1_insert_result = connection.execute(entity1.insert())
    print(entity1_insert_result)

""" Query
"""
with db.Connection(connection_string) as connection:
    entity1_select_result = connection.execute(entity1.select()).fetchall()
    print(entity1_select_result)


