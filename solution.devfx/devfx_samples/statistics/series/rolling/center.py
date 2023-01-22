import numpy as np
import pandas as pd
import devfx.data_structures as ds
import devfx.statistics as stats
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""  
class DataGenerator(object):
    def __init__(self):
        pass

    def generate(self, M):
        x = np.linspace(start=-4*3.14, stop=+4.0*3.14, num=1024)
        y = np.cos(x)*x + np.random.normal(0.0, 1.0, size=M)

        x = np.asarray(x).astype(dtype=np.float32)
        y = np.asarray(y).astype(dtype=np.float32)

        return ds.DataFrame.from_columns([x, y], columns=['x', 'y'])

"""------------------------------------------------------------------------------------------------
"""  
def test():
    data = DataGenerator().generate(1024)
    data['y_mean'] = stats.series.rolling.mean(data['y'], 64)
    data['y_ewmean'] = stats.series.rolling.ewmean(data['y'], 64)

    figure = dv.Figure(size=(8, 8), grid=(1,1))
    chart = dv.Chart2d(figure=figure, position=figure.grid[0,0])
    chart.plot(data['x'], data['y'])
    chart.plot(data['x'], data['y_mean'], 'red')
    chart.plot(data['x'], data['y_ewmean'], 'green')
    figure.show()

"""------------------------------------------------------------------------------------------------
"""  
if __name__ == '__main__':
    test()