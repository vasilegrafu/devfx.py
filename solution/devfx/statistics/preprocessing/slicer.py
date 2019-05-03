import numpy as np
import pandas as pd
import devfx.exceptions as exps
import devfx.reflection as refl

class Slicer(object):
    def __init__(self, start=None, stop=None, step=None):
        self.__start = start
        self.__stop = stop
        self.__step = step

    @property
    def start(self):
        return self.__start

    @property
    def stop(self):
        return self.__stop

    @property
    def step(self):
        return self.__step


    def slice(self, data):
        if (refl.is_typeof(data, tuple)):
            random_data = []
            for data_i in data:
                random_data.append(data_i[self.start:self.stop:self.step])
            random_data = tuple(random_data)
            return random_data

        if (refl.is_typeof(data, list)):
            random_data = []
            for data_i in data:
                random_data.append(data_i[self.start:self.stop:self.step])
            random_data = list(random_data)
            return random_data

        if(refl.is_typeof(data, dict)):
            random_data = {}
            for key in data:
                random_data[key] = data[key][self.start:self.stop:self.step]
            return random_data

        if(refl.is_typeof(data, np.ndarray)):
            random_data = data[self.start:self.stop:self.step]
            return random_data

        if (refl.is_typeof(data, pd.Series)):
            random_data = data[self.start:self.stop:self.step]
            return random_data

        if (refl.is_typeof(data, pd.DataFrame)):
            random_data = data[self.start:self.stop:self.step]
            return random_data

        raise exps.NotImplementedError()


# data = {
#     'x': np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
#     'y': np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# }
#
# sliced_data = Slicer(step=-1).slice(data=data)
# print(sliced_data)
#
#
# data = (np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
#         np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
#
# sliced_data = Slicer(stop=2).slice(data=data)
# print(sliced_data)

