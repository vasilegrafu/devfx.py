import numpy as np
import devfx.os as os
import devfx.databases.hdf5 as db
import devfx.data_vizualization.seaborn as dv

"""------------------------------------------------------------------------------------------------
"""
class MnistDataImporter(object):
    def __init__(self):
        pass

    def __load_data_from(self, source_path):
        data = os.file.read_text(source_path, encoding='utf-8', readlines=True)
        images = []
        labels = []
        for entry in data:
            entrybits = entry.split(',')
            image = np.asarray(entrybits[1:], dtype=np.uint8).reshape(28,28,1)
            label = np.asarray([int(entrybits[0])])
            images.append(image)
            labels.append(label)
        return [images, labels]

    def __save_data_to(self, data, destination_path):
        with db.File(destination_path) as file:
            images_dataset = file.create_dataset(path='/images', shape=(0,28,28,1), max_shape=(None,28,28,1), dtype=np.uint8)
            labels_dataset = file.create_dataset(path='/labels', shape=(0,1), max_shape=(None,1), dtype=np.uint8)
            for i in range(0, len(data[0])):
                if (len(images_dataset) < (i + 1)):
                    images_dataset.resize(((i + 1),28,28,1))
                images_dataset[i] = data[0][i]
                if (len(labels_dataset) < (i + 1)):
                    labels_dataset.resize(((i + 1),1))
                labels_dataset[i] = data[1][i]
                if (i % 100 == 0):
                    print(i)

    def import_data(self, source_path, destination_path):
        training_data = self.__load_data_from(os.path.join(source_path, 'mnist_train.csv'))
        self.__save_data_to(data=training_data, destination_path=os.path.join(destination_path, 'mnist_train.hdf5'))

        test_data = self.__load_data_from(os.path.join(source_path, 'mnist_test.csv'))
        self.__save_data_to(data=test_data, destination_path=os.path.join(destination_path, 'mnist_test.hdf5'))

if __name__ == '__main__':
    source_path = 'i:/Dev.Databases/mnist'
    destination_path = 'i:/Dev.Databases/mnist'
    
    MnistDataImporter().import_data(source_path, destination_path)
