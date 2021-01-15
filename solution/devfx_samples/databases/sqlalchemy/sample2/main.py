import datetime as dt
from devfx_samples.databases.sqlalchemy.sample2 import database as db
from devfx_samples.databases.sqlalchemy.sample2 import configuration as config

"""------------------------------------------------------------------------------------------------
"""
if __name__ == "__main__":
    with db.DatabaseSession(config) as dbsession:
        for granularity_code in config.candlesticks.granularity_codes:
            granularity = db.GranularityCtrl(dbsession).getByCode(granularity_code)
            if(granularity is None):
                granularity = db.Granularity(code=granularity_code)
                db.GranularityCtrl(dbsession).save(granularity)

    with db.DatabaseSession(config) as dbsession:
        for granularity in db.GranularityCtrl(dbsession).getAll():
            if(granularity.code not in config.candlesticks.granularity_codes):
                db.GranularityCtrl(dbsession).deleteByCode(granularity.code)


    with db.DatabaseSession(config) as dbsession:
        for instrument_code in config.candlesticks.instrument_codes:
            instrument = db.InstrumentCtrl(dbsession).getByCode(instrument_code)
            if(instrument is None):
                instrument = db.Instrument(code=instrument_code)
                db.InstrumentCtrl(dbsession).save(instrument)

    with db.DatabaseSession(config) as dbsession:
        for instrument in db.InstrumentCtrl(dbsession).getAll():
            if(instrument.code not in config.candlesticks.instrument_codes):
                db.InstrumentCtrl(dbsession).deleteByCode(instrument.code)


    with db.DatabaseSession(config) as dbsession:
        instrument = db.InstrumentCtrl(dbsession).getByCode('EUR_USD')
        granularity = db.GranularityCtrl(dbsession).getByCode('M1')

        candlestick = db.Candlestick(instrument_id=instrument.id,
                                        granularity_id=granularity.id,
                                        datetime=dt.datetime.utcnow(),
                                        open=2.0,
                                        close=2.0,
                                        high=4.0,
                                        low=1.0,
                                        spread=0.2,
                                        volume=100,
                                        complete=True)

        db.CandlestickCtrl(dbsession).save(candlestick)