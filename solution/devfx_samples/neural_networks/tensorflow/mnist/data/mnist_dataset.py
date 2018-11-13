import numpy as np
import devfx.os as os
import devfx.databases.hdf5 as db
import devfx.data_containers.dataset as dc
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class MnistDataset(dc.Dataset):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _on_getitem_data_filter(self, data, hparams):
        indexes = data[0]
        data_file = hparams[0]

        images = np.asarray(data_file['/images'][sorted(indexes)])
        labels = np.asarray(data_file['/labels'][sorted(indexes)])

        return [images, labels]

"""------------------------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    data_path = 'i:/Dev.Databases/mnist'

    training_data_file = None
    test_data_file = None
    try:
        training_data_file = db.File(os.path.join(data_path, 'mnist_train.hdf5'))
        training_dataset = MnistDataset(data=[list(range(training_data_file['/images'].shape[0]))], hparams=[training_data_file])

        test_data_file = db.File(os.path.join(data_path, 'mnist_test.hdf5'))
        test_dataset = MnistDataset(data=[list(range(test_data_file['/images'].shape[0]))], hparams=[test_data_file])

        print(training_dataset[:2], test_dataset[[0, 2]])

        figure = dv.Figure(size=(8, 8))
        chart = dv.Chart2d(figure=figure)
        chart.image(training_dataset[0:1][0][0].reshape(28,28), cmap='Greys', interpolation='None')
        figure.show()
    finally:
        if (test_data_file is not None): test_data_file.close()
        if (training_data_file is not None): training_data_file.close()
