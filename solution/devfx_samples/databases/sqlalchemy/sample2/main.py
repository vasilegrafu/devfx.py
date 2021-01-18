import datetime as dt
from devfx_samples.databases.sqlalchemy.sample2 import database as db
from devfx_samples.databases.sqlalchemy.sample2 import configuration as config

"""------------------------------------------------------------------------------------------------
"""
if __name__ == "__main__":
    with db.Session(config) as session:
        for granularity_code in config.candlesticks.granularity_codes:
            granularity = db.GranularityCtrl(session).getByCode(granularity_code)
            if(granularity is None):
                granularity = db.Granularity(code=granularity_code)
                db.GranularityCtrl(session).save(granularity)

    with db.Session(config) as session:
        for granularity in db.GranularityCtrl(session).getAll():
            if(granularity.code not in config.candlesticks.granularity_codes):
                db.GranularityCtrl(session).deleteByCode(granularity.code)


    with db.Session(config) as session:
        for instrument_code in config.candlesticks.instrument_codes:
            instrument = db.InstrumentCtrl(session).getByCode(instrument_code)
            if(instrument is None):
                instrument = db.Instrument(code=instrument_code)
                db.InstrumentCtrl(session).save(instrument)

    with db.Session(config) as session:
        for instrument in db.InstrumentCtrl(session).getAll():
            if(instrument.code not in config.candlesticks.instrument_codes):
                db.InstrumentCtrl(session).deleteByCode(instrument.code)


    with db.Session(config) as session:
        instrument = db.InstrumentCtrl(session).getByCode('EUR_USD')
        granularity = db.GranularityCtrl(session).getByCode('M1')

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

        db.CandlestickCtrl(session).save(candlestick)