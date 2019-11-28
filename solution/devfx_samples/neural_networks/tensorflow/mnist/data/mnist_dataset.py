import numpy as np
import devfx.os as os
import devfx.databases.hdf5 as db
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class MnistDataLoader(object):
    def __init__(self, data_file):
        self.__data_file = data_file

    def load(self):
        indices = list(range(self.__data_file['/images'].shape[0]))

        images = np.asarray(self.__data_file['/images'][sorted(indices)])
        labels = np.asarray(self.__data_file['/labels'][sorted(indices)])

        return [images, labels]

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    data_path = 'i:/Dev.Databases/mnist'

    with db.File(os.path.join(data_path, 'mnist_train.hdf5')) as data_file:
        training_data = MnistDataLoader(data_file=data_file).load()

    with db.File(os.path.join(data_path, 'mnist_test.hdf5')) as data_file:
        test_data = MnistDataLoader(data_file=data_file).load()

    figure = dv.Figure(size=(8, 8))
    chart = dv.Chart2d(figure=figure)
    chart.image(training_data[0][1].reshape(28,28), cmap='Greys', interpolation='None')
    figure.show()

