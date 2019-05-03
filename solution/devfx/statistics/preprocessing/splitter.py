import numpy as np
import pandas as pd
import devfx.exceptions as exps
import devfx.reflection as refl

class Splitter(object):
    def __init__(self, ratios=(0.75,)):
        if(not refl.is_iterable(ratios)):
            raise exps.ArgumentError()
        ratios = np.asarray(ratios)
        for ratio in ratios:
            if(not (0 <= ratio <= 1)):
                raise exps.ArgumentError()
        if(not (np.diff(ratios) >= 0).all()):
            raise exps.ArgumentError()
        self.__ratios = ratios

    @property
    def ratios(self):
        return self.__ratios

    def split(self, data):
        if(refl.is_typeof_tuple(data)):
            data_splitted_1 = []
            for data_i in data:
                data_splitted_1.append(Splitter(ratios=self.ratios).split(data_i))
            data_splitted_2 = []
            for i in range(len(self.ratios) + 1):
                _ = []
                r = 0
                while r <= (len(data_splitted_1) - 1):
                    _.append(data_splitted_1[r][i])
                    r += 1
                data_splitted_2.append(tuple(_))
            return data_splitted_2

        if(refl.is_typeof_list(data)):
            data_splitted_1 = []
            for data_i in data:
                data_splitted_1.append(Splitter(ratios=self.ratios).split(data_i))
            data_splitted_2 = []
            for i in range(len(self.ratios) + 1):
                _ = []
                r = 0
                while r <= (len(data_splitted_1) - 1):
                    _.append(data_splitted_1[r][i])
                    r += 1
                data_splitted_2.append(list(_))
            return data_splitted_2

        if(refl.is_typeof_dict(data)):
            data_splitted_1 = {}
            for key in data:
                data_splitted_1[key] = Splitter(ratios=self.ratios).split(data[key])
            data_splitted_2 = []
            for i in range(len(self.ratios) + 1):
                _ = {}
                for key in data_splitted_1:
                    _[key] = data_splitted_1[key][i]
                data_splitted_2.append(_)
            return data_splitted_2

        if(refl.is_typeof(data, np.ndarray)):
            bounds = np.int32(len(data)*self.ratios)
            data_splitted = []
            i = 0
            while i <= (len(bounds)-1):
                if(i == 0):
                    data_splitted.append(data[:bounds[i]])
                else:
                    data_splitted.append(data[bounds[i-1]:bounds[i]])
                i += 1
            data_splitted.append(data[bounds[-1]:])
            return data_splitted

        if (refl.is_typeof(data, pd.Series)):
            bounds = np.int32(len(data)*self.ratios)
            data_splitted = []
            i = 0
            while i <= (len(bounds)-1):
                if(i == 0):
                    data_splitted.append(data[:bounds[i]])
                else:
                    data_splitted.append(data[bounds[i-1]:bounds[i]])
                i += 1
            data_splitted.append(data[bounds[-1]:])
            return data_splitted

        if (refl.is_typeof(data, pd.DataFrame)):
            bounds = np.int32(len(data.index)*self.ratios)
            data_splitted = []
            i = 0
            while i <= (len(bounds)-1):
                if(i == 0):
                    data_splitted.append(data[:bounds[i]])
                else:
                    data_splitted.append(data[bounds[i-1]:bounds[i]])
                i += 1
            data_splitted.append(data[bounds[-1]:])
            return data_splitted

        raise exps.NotImplementedError()


# data = {
#     'x': np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
#     'y': np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# }
#
# splitted_data = Splitter().split(data=data)
# print(splitted_data)


# data = (np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
#         np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
#
# splitted_data = Splitter().split(data=data)
# print(splitted_data)



