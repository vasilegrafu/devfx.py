import h5py as h5
import numpy as np

f = h5.File('./data/compressed_dataset.hdf5', mode='a')

compressed_dataset = f.create_dataset("comp3", shape=(1024,2), dtype='int32', compression='gzip')
compressed_dataset = f['comp3']

for i in np.arange(compressed_dataset.shape[0]):
    for j in np.arange(compressed_dataset.shape[1]):
        compressed_dataset[i,j] = i + j
print(compressed_dataset[[1, 3]])