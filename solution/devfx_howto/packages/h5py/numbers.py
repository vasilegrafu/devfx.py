import h5py as h5
import numpy as np

#
numbers = np.random.random(1024)

f = h5.File('./data/numbers.hdf5', mode='a')

f["/dir1/numbers"] = numbers
f["/dir1/numbers"].attrs["dt"] = 10.0
f["/dir1/numbers"].attrs["start_time"] = '2018-02-18'

dataset = f['/dir1/numbers']
for (name, value) in dataset.attrs.items():
     print(name, value)

print(dataset[0:10])

#
compressed_dataset = f.create_dataset("comp3", shape=(1024,2), dtype='int32', compression='gzip')
compressed_dataset = f['comp3']

for i in np.arange(compressed_dataset.shape[0]):
    for j in np.arange(compressed_dataset.shape[1]):
        compressed_dataset[i,j] = i + j
print(compressed_dataset[[1, 3]])