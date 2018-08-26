import numpy as np
import pandas as pd
import devfx.exceptions as exceptions
import devfx.reflection as refl


class Shuffler(object):
    def __init__(self):
        pass

    def shuffle(self, data):
        if(refl.is_typeof(data, tuple)):
            random_indexes = np.random.choice(np.arange(0, len(data[0])), size=len(data[0]), replace=False)
            random_data = []
            for data_i in data:
                random_data.append(data_i[random_indexes])
            random_data = tuple(random_data)
            return random_data

        if(refl.is_typeof(data, list)):
            random_indexes = np.random.choice(np.arange(0, len(data[0])), size=len(data[0]), replace=False)
            random_data = []
            for data_i in data:
                random_data.append(data_i[random_indexes])
            random_data = list(random_data)
            return random_data

        if(refl.is_typeof(data, dict)):
            random_indexes = np.random.choice(np.arange(0, data[list(data.keys())[0]].size), size=data[list(data.keys())[0]].size, replace=False)
            random_data = {}
            for key in data:
                random_data[key] = data[key][random_indexes]
            return random_data

        if(refl.is_typeof(data, np.ndarray)):
            random_indexes = np.random.choice(np.arange(0, len(data)), size=len(data), replace=False)
            random_data = data[random_indexes]
            return random_data

        if(refl.is_typeof(data, pd.Series)):
            random_indexes = np.random.choice(np.arange(0, len(data)), size=len(data), replace=False)
            random_data = data[random_indexes]
            return random_data

        if(refl.is_typeof(data, pd.DataFrame)):
            random_indexes = np.random.choice(np.arange(0, len(data)), size=len(data), replace=False)
            random_data = data[random_indexes]
            return random_data

        raise exceptions.NotImplementedError()


data = {
    'x': np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    'y': np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
}

shuffled_data = Shuffler().shuffle(data=data)
print(shuffled_data)


data = (np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

shuffled_data = Shuffler().shuffle(data=data)
print(shuffled_data)

