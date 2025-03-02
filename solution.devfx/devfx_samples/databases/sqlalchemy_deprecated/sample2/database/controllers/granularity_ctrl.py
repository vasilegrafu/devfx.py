import devfx.databases.sqlalchemy as sa
from ..models import Granularity

"""------------------------------------------------------------------------------------------------
"""
class GranularityCtrl(object):
    def __init__(self, session):
        self.__session = session

    """----------------------------------------------------------------
    """
    def save(self, instance):
        existing_instance = self.getByCode(instance.code)
        if(existing_instance is not None):
            existing_instance.copy_from(instance)
        else:
            self.__session.add(instance)

    def saveAll(self, instances):
        for instance in instances:
            self.save(instance)

    """----------------------------------------------------------------
    """
    def deleteById(self, id):
        self.__session.delete(self.getById(id))

    def deleteByCode(self, code):
        self.__session.delete(self.getByCode(code))

    """----------------------------------------------------------------
    """
    def getById(self, id, projection=(Granularity, )):
        return self.__session.query(*projection) \
                    .filter(Granularity.id == id) \
                    .one_or_none()

    """----------------------------------------------------------------
    """
    def getByCode(self, code, projection=(Granularity, )):
        return self.__session.query(*projection) \
                    .filter(Granularity.code == code) \
                    .one_or_none()

    """----------------------------------------------------------------
    """
    def getAll(self, projection=(Granularity, )):
        return self.__session.query(*projection) \
                    .to_list()

    """------------------------------------------------------------------------------------------------
    """
    class __querier(object):
        def __init__(self, session):
            self.__session = session

        """----------------------------------------------------------------
        """
        def getAll(self, projection=(Granularity, ), index_col=None):
            return self.__session.query(*projection) \
                        .to_dataframe(index_col=index_col)

    """----------------------------------------------------------------
    """
    @property
    def querier(self):
        return GranularityCtrl.__querier(self.__session)