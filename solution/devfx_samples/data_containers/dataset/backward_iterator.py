import numpy as np
import devfx.data_containers as dc

v = [np.arange(0, 10, 1), 2*np.arange(0, 10, 1)]
print(v)

ds = dc.Dataset(v, iterator_kind=dc.DatasetIteratorKind.BACKWARD)
ds_iterator = ds.iterator(batch_size=4)

ds_iterator_data = ds_iterator.next()
print(ds_iterator_data)

ds_iterator_data = ds_iterator.next()
print(ds_iterator_data)

ds_iterator_data = ds_iterator.next()
print(ds_iterator_data)