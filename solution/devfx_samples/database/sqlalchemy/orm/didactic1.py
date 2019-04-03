import datetime as dt
import devfx.databases.sqlalchemy as db

BaseDatabaseEntity = db.orm.create_base_database_entity_type()

""" Schema
"""
class Entity1(BaseDatabaseEntity):
    __tablename__ = "entity1"

    id = db.orm.Column_as__Integer_id()
    entity2s = db.orm.Relationship_one_to_many("Entity2")

    created_on = db.orm.Column_as__created_on()
    updated_on = db.orm.Column_as__updated_on()

    def __repr__(self):
        return "Entity1(id={self.id}, "\
                    "created_on={self.created_on}, "\
                    "created_on={self.updated_on})".format(self=self)


class Entity2(BaseDatabaseEntity):
    __tablename__ = "entity2"
    id = db.orm.Column_as__Integer_id()
    entity1_id = db.orm.Column_as_ForeignKey("entity1.id")
    entity1 = db.orm.Relationship_many_to_one("Entity1")

    BigInteger = db.orm.Column_as_BigInteger()
    Integer = db.orm.Column_as_Integer()
    SmallInteger = db.orm.Column_as_SmallInteger()
    FixedPointNumber = db.orm.Column_as_FixedPointNumber()
    FloatingPointNumber = db.orm.Column_as_FloatingPointNumber()

    String = db.orm.Column_as_String()
    Text = db.orm.Column_as_Text()

    Boolean = db.orm.Column_as_Boolean()

    DateTime = db.orm.Column_as_DateTime()
    Date = db.orm.Column_as_Date()
    Time = db.orm.Column_as_Time()
    Timedelta = db.orm.Column_as_Timedelta()

    created_on = db.orm.Column_as__created_on()
    updated_on = db.orm.Column_as__updated_on()

    def __repr__(self):
        return "Entity2(id={self.id}, "\
                "id_entity1={self.entity1_id}, " \
                "BigInteger={self.BigInteger}, " \
                "Integer={self.Integer}, "\
                "SmallInteger={self.SmallInteger}, "\
                "FixedPointNumber={self.FixedPointNumber}, "\
                "FloatingPointNumber={self.FloatingPointNumber}, "\
                "String='{self.String}', " \
                "Text='{self.Text}', " \
                "Boolean={self.Boolean}, "\
                "DateTime={self.DateTime}, "\
                "Date={self.Date}, "\
                "Time={self.Time}, "\
                "Timedelta={self.Timedelta}, "\
                "created_on={self.created_on}, "\
                "created_on={self.updated_on})".format(self=self)


""" Connection string
"""
database_connection_string = 'sqlite:///devfx_samples/database/sqlalchemy/orm/didactic1.db'

""" Deploy
"""
db.orm.deploy_database_metadata(BaseDatabaseEntity, database_connection_string)


""" Create
"""
with db.orm.Session(database_connection_string) as session:
    entity11 = Entity1()
    session.add(entity11)
    session.flush()

    entity21 = Entity2()
    entity21.entity1_id = entity11.id
    entity21.BigInteger = 1
    entity21.Integer = 1
    entity21.SmallInteger = 1
    entity21.FixedPointNumber = 1
    entity21.FloatingPointNumber = 1.0
    entity21.String = "1"
    entity21.UnicodeString = "1"
    entity21.Text = "1"
    entity21.UnicodeText = "1"
    entity21.Boolean = True
    entity21.DateTime = dt.datetime.utcnow()
    entity21.Date = entity21.DateTime.date()
    entity21.Time = entity21.DateTime.time()
    entity21.Timedelta = dt.timedelta(seconds=8)
    session.add(entity21)
    session.flush()

    entity22 = Entity2()
    entity22.entity1_id = entity11.id
    entity22.BigInteger = 2
    entity22.Integer = 2
    entity22.SmallInteger = 2
    entity22.FixedPointNumber = 2
    entity22.FloatingPointNumber = 1.0
    entity22.String = "2"
    entity22.UnicodeString = "2"
    entity22.Text = "2"
    entity22.UnicodeText = "2"
    entity22.Boolean = True
    entity22.DateTime = dt.datetime.utcnow()
    entity22.Date = entity21.DateTime.date()
    entity22.Time = entity21.DateTime.time()
    entity22.Timedelta = dt.timedelta(seconds=8)
    session.add(entity22)
    session.flush()

""" Query
"""
with db.orm.Session(database_connection_string) as session:
    entity1_list = session.query(Entity1.id).all()
    for entity1 in entity1_list:
        print(entity1)

    entity2_list = session.query(Entity2).all()
    for entity2 in entity2_list:
        print(entity2)

""" Update
"""
with db.orm.Session(database_connection_string) as session:
    entity2_list = session.query(Entity2).all()
    for entity2 in entity2_list:
        entity2.Integer = entity2.Integer+1

""" Delete
"""
# with db.orm.Session(database_connection_string) as session:
#     entity1 = session.query(Entity1).first()
#     session.delete(entity1)


""" Relationship
"""
with db.orm.Session(database_connection_string) as session:
    entity1 = session.query(Entity1).first()
    print(entity1.entity2s)
    entity2 = session.query(Entity2).first()
    print(entity2.entity1)