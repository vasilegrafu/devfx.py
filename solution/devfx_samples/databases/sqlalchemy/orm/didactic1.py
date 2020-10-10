import datetime as dt
import devfx.databases.sqlalchemy as sadb

BaseDatabaseEntity = sadb.orm.create_base_database_entity_type()

""" Schema
"""
class Entity1(BaseDatabaseEntity):
    __tablename__ = "entity1"

    id = sadb.orm.Column_as__Integer_id()
    entity2s = sadb.orm.Relationship_one_to_many("Entity2")

    created_on = sadb.orm.Column_as__created_on()
    updated_on = sadb.orm.Column_as__updated_on()

    def __repr__(self):
        return "Entity1(id={self.id}, "\
                    "created_on={self.created_on}, "\
                    "created_on={self.updated_on})".format(self=self)


class Entity2(BaseDatabaseEntity):
    __tablename__ = "entity2"
    id = sadb.orm.Column_as__Integer_id()
    entity1_id = sadb.orm.Column_as_ForeignKey("entity1.id")
    entity1 = sadb.orm.Relationship_many_to_one("Entity1")

    BigInteger = sadb.orm.Column_as_BigInteger()
    Integer = sadb.orm.Column_as_Integer()
    SmallInteger = sadb.orm.Column_as_SmallInteger()
    FixedPointNumber = sadb.orm.Column_as_FixedPointNumber()
    FloatingPointNumber = sadb.orm.Column_as_FloatingPointNumber()

    String = sadb.orm.Column_as_String()
    Text = sadb.orm.Column_as_Text()

    Boolean = sadb.orm.Column_as_Boolean()

    DateTime = sadb.orm.Column_as_DateTime()
    Date = sadb.orm.Column_as_Date()
    Time = sadb.orm.Column_as_Time()
    Timedelta = sadb.orm.Column_as_Timedelta()

    created_on = sadb.orm.Column_as__created_on()
    updated_on = sadb.orm.Column_as__updated_on()

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
connection_string = 'sqlite:///devfx_samples/database/sqlalchemy/orm/didactic1.db'

""" Deploy
"""
sadb.orm.deploy_database_metadata(BaseDatabaseEntity, connection_string)


""" Create
"""
with sadb.orm.DatabaseSession(connection_string) as session:
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
with sadb.orm.DatabaseSession(connection_string) as dbsession:
    entity1_list = dbsession.query(Entity1.id).all()
    for entity1 in entity1_list:
        print(entity1)

    entity2_list = dbsession.query(Entity2).all()
    for entity2 in entity2_list:
        print(entity2)

""" Update
"""
with sadb.orm.DatabaseSession(connection_string) as dbsession:
    entity2_list = dbsession.query(Entity2).all()
    for entity2 in entity2_list:
        entity2.Integer = entity2.Integer+1

""" Delete
"""
# with sadb.orm.DatabaseSession(database_connection_string) as dbsession:
#     entity1 = dbsession.query(Entity1).first()
#     dbsession.delete(entity1)


""" Relationship
"""
with sadb.orm.DatabaseSession(connection_string) as dbsession:
    entity1 = dbsession.query(Entity1).first()
    print(entity1.entity2s)
    entity2 = dbsession.query(Entity2).first()
    print(entity2.entity1)