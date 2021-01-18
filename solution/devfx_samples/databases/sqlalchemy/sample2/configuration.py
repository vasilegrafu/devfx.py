
"""------------------------------------------------------------------------------------------------
"""
class candlesticks(object):
    """ Value 	Description
        S5 	    5 second candlesticks,      minute alignment
        S10 	10 second candlesticks,     minute alignment
        S15 	15 second candlesticks,     minute alignment
        S30 	30 second candlesticks,     minute alignment
        M1 	    1 minute candlesticks,      minute alignment
        M2 	    2 minute candlesticks,      hour alignment
        M4 	    4 minute candlesticks,      hour alignment
        M5 	    5 minute candlesticks,      hour alignment
        M10 	10 minute candlesticks,     hour alignment
        M15 	15 minute candlesticks,     hour alignment
        M30 	30 minute candlesticks,     hour alignment
        H1 	    1 hour candlesticks,        hour alignment
        H2 	    2 hour candlesticks,        day alignment
        H3 	    3 hour candlesticks,        day alignment
        H4 	    4 hour candlesticks,        day alignment
        H6 	    6 hour candlesticks,        day alignment
        H8 	    8 hour candlesticks,        day alignment
        H12 	12 hour candlesticks,       day alignment
        D 	    1 day candlesticks,         day alignment
        W 	    1 week candlesticks,        aligned to start of week
        M 	    1 month candlesticks,       aligned to first day of the month
    """
    granularity_codes = [
        'S5', 'S10', 'S15', 'S30',
        'M1', 'M2', 'M4', 'M5', 'M10', 'M15', 'M30',
        'H1', 'H2', 'H3', 'H4', 'H6', 'H8', 'H12',
        'D',
        'W',
        'M'
    ]

    """ 'EUR_ZAR'
        'EUR_PLN'
        'AUD_JPY'
        'USD_CAD'
        'USD_NOK'
        'CAD_SGD'
        'HKD_JPY'
        'NZD_JPY'
        'USD_HUF'
        'CHF_ZAR'
        'EUR_CZK'
        'AUD_HKD'
        'GBP_NZD'
        'NZD_HKD'
        'NZD_CHF'
        'USD_SAR'
        'GBP_CAD'
        'CAD_JPY'
        'ZAR_JPY'
        'NZD_SGD'
        'GBP_ZAR'
        'NZD_CAD'
        'CAD_HKD'
        'SGD_CHF'
        'CAD_CHF'
        'AUD_SGD'
        'EUR_NOK'
        'EUR_CHF'
        'GBP_USD'
        'USD_MXN'
        'USD_CHF'
        'AUD_CHF'
        'EUR_DKK'
        'AUD_USD'
        'CHF_HKD'
        'USD_THB'
        'GBP_CHF'
        'TRY_JPY'
        'AUD_CAD'
        'SGD_JPY'
        'EUR_NZD'
        'USD_HKD'
        'EUR_AUD'
        'USD_DKK'
        'CHF_JPY'
        'EUR_SGD'
        'USD_SGD'
        'EUR_SEK'
        'USD_JPY'
        'EUR_TRY'
        'USD_CZK'
        'GBP_AUD'
        'USD_PLN'
        'EUR_USD'
        'AUD_NZD'
        'SGD_HKD'
        'EUR_HUF'
        'NZD_USD'
        'USD_CNH'
        'EUR_HKD'
        'EUR_JPY'
        'GBP_PLN'
        'GBP_JPY'
        'USD_TRY'
        'EUR_CAD'
        'USD_SEK'
        'GBP_SGD'
        'EUR_GBP'
        'GBP_HKD'
        'USD_ZAR'
    """
    instrument_codes = [
        'EUR_USD'# ,
        # 'EUR_GBP',
        # 'EUR_CHF',
        # 'EUR_JPY',
        # 'GBP_USD',
        # 'GBP_CHF',
        # 'GBP_JPY',
        # 'USD_CHF',
        # 'USD_JPY',
        # 'CHF_JPY'
    ]

class database(object):
    url = 'sqlite:///devfx_samples/databases/sqlalchemy/sample2/database.db'