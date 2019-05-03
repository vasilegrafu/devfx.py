import devfx.data_containers as dc 
import devfx.statistics as stats
import devfx.data_vizualization.seaborn as dv
import config as cfg

"""------------------------------------------------------------------------------------------------
"""
def main():
    #
    quotes = dc.DataFrame.from_csv(cfg.Config.csv.file_path, 
                                   usecols=['datetime', 'open', 'high', 'low', 'close', 'spread', 'volume'], 
                                   index_col=['datetime'],
                                   parse_dates=['datetime'])

    candlesticks = quotes[['open', 'high', 'low', 'close']][0:256]
    volumes = quotes['volume'][0:256]

    closes_rolling_mean10 = stats.rolling_mean(candlesticks['close'], 10)
    closes_rolling_mean20 = stats.rolling_mean(candlesticks['close'], 20)

    #
    figure = dv.Figure(size=(8, 6), grid=(2, 1))

    chart = dv.Chart2d(figure=figure, position=figure[0,0])
    chart.timeseries.candlesticks(candlesticks)
    chart.timeseries.plot(closes_rolling_mean10)
    chart.timeseries.plot(closes_rolling_mean20)

    chart = dv.Chart2d(figure=figure, position=figure[1,0])     
    chart.timeseries.bar(volumes)

    figure.show()

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    main()
