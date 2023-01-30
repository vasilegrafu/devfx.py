import datetime as dt
import devfx.exceptions as ex
import devfx.core as core
import devfx.databases.sqlalchemy as sa
from ..models import Candlestick
from ..controllers import InstrumentCtrl
from ..controllers import GranularityCtrl

"""------------------------------------------------------------------------------------------------
"""
class CandlestickCtrl(object):
    def __init__(self, session):
        self.__session = session

    """----------------------------------------------------------------
    """
    def save(self, instance):
        existing_instance = self.getByDatetime(instance.instrument_id, instance.granularity_id, instance.datetime)
        if(existing_instance is not None):
            existing_instance.copy_from(instance)
        else:
            self.__session.add(instance)

    def saveAll(self, instances):
        not_existing_instances = []
        existing_instances = self.getByKeys([(_.instrument_id, _.granularity_id, _.datetime) for _ in instances])
        for instance in instances:
            existing_instance_found = None
            for existing_instance in existing_instances:
                if(existing_instance.instrument_id == instance.instrument_id and existing_instance.granularity_id == instance.granularity_id and existing_instance.datetime == instance.datetime):
                    existing_instance_found = existing_instance
                    break
            if(existing_instance_found is not None):
                existing_instance_found.copy_from(instance)
            else:
                not_existing_instances.append(instance)
        self.__session.add_all(not_existing_instances)

    """----------------------------------------------------------------
    """
    def deleteById(self, id):
        self.__session.delete(self.getById(id))


    """----------------------------------------------------------------
    """
    def getById(self, id, projection=(Candlestick, )):
        result = self.__session.query(*projection) \
                    .filter(Candlestick.id == id) \
                    .one_or_none()
        return result

    """----------------------------------------------------------------
    """
    def getByKey(self, key, projection=(Candlestick, )):
        result = self.__session.query(*projection) \
                    .filter((Candlestick.instrument_id == key[0])
                            & (Candlestick.granularity_id == key[1])
                            & (Candlestick.datetime == key[2])) \
                    .one_or_none()
        return result

    def getByKeys(self, keys, projection=(Candlestick, )):
        result = []
        n = 250
        key_segments = [keys[i * n:(i + 1) * n] for i in range((len(keys) + n - 1) // n )]
        for key_segment in key_segments:
            query = self.__session.query(*projection)
            and_conditions = []
            for key in key_segment:
                and_condition = sa.and_(Candlestick.instrument_id == key[0],
                                          Candlestick.granularity_id == key[1],
                                          Candlestick.datetime == key[2])
                and_conditions.append(and_condition)
            or_condition = sa.or_(*and_conditions)
            segment_result = query.filter(or_condition) \
                                  .all()
            for _ in segment_result:
                result.append(_)
        return result

    """----------------------------------------------------------------
    """
    def getByDatetime(self, instrument_id, granularity_id, datetime, projection=(Candlestick, )):
        result = self.__session.query(*projection) \
                    .filter((Candlestick.instrument_id == instrument_id)
                            & (Candlestick.granularity_id == granularity_id)
                            & (Candlestick.datetime == datetime)) \
                    .one_or_none()
        return result
     
    """----------------------------------------------------------------
    """
    def getLatest(self, instrument_id, granularity_id, projection=(Candlestick, )):
        result = self.__session.query(*projection) \
                    .filter((Candlestick.instrument_id == instrument_id) 
                            & (Candlestick.granularity_id == granularity_id)) \
                    .order_by(Candlestick.datetime.desc()) \
                    .limit(1)\
                    .one_or_none()
        return result

    """----------------------------------------------------------------
    """
    def getFirst(self, instrument_id, granularity_id, projection=(Candlestick, )):
        result = self.__session.query(*projection) \
                    .filter((Candlestick.instrument_id == instrument_id) 
                            & (Candlestick.granularity_id == granularity_id)) \
                    .order_by(Candlestick.datetime.asc()) \
                    .limit(1)\
                    .one_or_none()
        return result

    """----------------------------------------------------------------
    """
    def getAll(self, projection=(Candlestick, )):
        result = self.__session.query(*projection) \
                    .to_list()
        return result


    """------------------------------------------------------------------------------------------------
    """
    class __querier(object):
        def __init__(self, session):
            self.__session = session

       
        """----------------------------------------------------------------
        """
        def getAllInInterval(self, instrument_code, granularity_code, interval=None, projection=(Candlestick, )):
            instrument_id = InstrumentCtrl(self.__session).getByCode(code=instrument_code).id
            granularity_id = GranularityCtrl(self.__session).getByCode(code=granularity_code).id

            query = self.__session.query(*projection) \
                        .join(Candlestick.instrument) \
                        .join(Candlestick.granularity) \
            
            # latestN until datetime
            if(core.is_typeof(interval[0], int) and core.is_typeof(interval[1], dt.datetime)):
                query = query.filter((Candlestick.instrument_id == instrument_id)
                                     & (Candlestick.granularity_id == granularity_id)
                                     & (Candlestick.datetime <= interval[1])) \
                             .order_by(Candlestick.datetime.desc()) \
                             .limit(interval[0])
            # latestN
            elif(core.is_typeof(interval[0], int) and interval[1] is None):
                query = query.filter((Candlestick.instrument_id == instrument_id)
                                     & (Candlestick.granularity_id == granularity_id)) \
                             .order_by(Candlestick.datetime.desc()) \
                             .limit(interval[0])
            # firstN since datetime
            elif(core.is_typeof(interval[0], dt.datetime) and core.is_typeof(interval[1], int)):
                query = query.filter((Candlestick.instrument_id == instrument_id)
                                     & (Candlestick.granularity_id == granularity_id)
                                     & (Candlestick.datetime >= interval[0])) \
                             .limit(interval[0])
            # firstN
            elif(interval[0] is None and core.is_typeof(interval[1], int)):
                query = query.filter((Candlestick.instrument_id == instrument_id)
                                     & (Candlestick.granularity_id == granularity_id)) \
                             .limit(interval[0])

            # in datetime interval
            elif(core.is_typeof(interval[0], dt.datetime) and core.is_typeof(interval[1], dt.datetime)):
                query = query.filter((Candlestick.instrument_id == instrument_id)
                                     & (Candlestick.granularity_id == granularity_id)
                                     & ((Candlestick.datetime >= interval[0]) & (Candlestick.datetime <= interval[1])))
            # incorrect argument
            else:
                raise ex.ArgumentError()
            
            return query

    """----------------------------------------------------------------
    """
    @property
    def querier(self):
        return CandlestickCtrl.__querier(self.__session)