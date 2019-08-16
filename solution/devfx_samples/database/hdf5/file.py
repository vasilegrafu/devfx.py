import numpy as np
import devfx.databases.hdf5 as hdf5db

file_path = 'devfx_samples/database/hdf5/C.hdf5'

with hdf5db.File(file_path) as file:
    value = np.asarray([[1, 2],
                        [3, 4]])
    file.set('/1/1', value)
    file.set('/1/2', value)
    file['/2/1'] = value
    file['2']['2'] = value

with hdf5db.File(file_path) as file:
    print(file.paths(max_depth=2))

with hdf5db.File(file_path) as file:
    file['/1/1'].attributes.set('a', 11)
    file['/1/2'].attributes.set('a', 12)
    file['/2/1'].attributes.set('a', 21)
    file['2']['2'].attributes.set('a', 22)

with hdf5db.File(file_path) as file:
    print(file.get('/1/1').attributes.get('a'))
    print(file.get('/1/2').attributes.get('a'))
    print(file.get('/2/1').attributes.get('a'))
    print(file.get('/2/2').attributes.get('a'))


with hdf5db.File(file_path) as file:
    print(file.get('/1/1'))
    print(file.get('/1/2'))
    print(file['/2/1'][...])
    print(file['/2/2'][...])

with hdf5db.File(file_path) as file:
    print(file.exists('/1/1'))
    print(file.exists('/1/2'))
    print(file.exists('/2/1'))
    print(file.exists('/2/2'))

with hdf5db.File(file_path) as file:
    print(file.remove('/1/1'))
    print(file.remove('/1/2'))
    print(file.remove('/2/1'))
    print(file.remove('/2/2'))

with hdf5db.File(file_path) as file:
    print(file.exists('/1/1'))
    print(file.exists('/1/2'))
    print(file.exists('/2/1'))
    print(file.exists('/2/2'))

