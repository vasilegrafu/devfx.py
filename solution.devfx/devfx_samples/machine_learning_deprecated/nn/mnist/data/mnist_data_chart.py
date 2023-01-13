import numpy as np
import devfx.os as os
import devfx.databases.hdf5 as db
import devfx.data_vizualization as dv

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    data_path = 'i:/Dev.Databases/mnist'

    training_data_file = db.File(os.path.join(data_path, 'mnist_train.hdf5'))
    training_data = [training_data_file.get_dataset('/images'), training_data_file.get_dataset('/labels')]

    test_data_file = db.File(os.path.join(data_path, 'mnist_test.hdf5'))
    test_data = [test_data_file.get_dataset('/images'), test_data_file.get_dataset('/labels')]

    figure = dv.Figure(size=(8, 8))
    chart = dv.Chart2d(figure=figure)
    chart.image(training_data[0][1], cmap='Greys', interpolation='None')
    figure.show()
