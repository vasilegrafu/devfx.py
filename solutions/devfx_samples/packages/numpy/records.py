import numpy as np

recordtype = np.dtype([('id', np.int32),
                       ('name', np.str, 256),
                       ('grades', np.float64, (2,)),
                       ('links', np.bool, (2,2)),
                       ('datetime', np.object)])

x = np.array([(1, "name1", [1.0, 1.0], [[True, True], [True, True]], np.datetime64('2016-12-30')),
              (2, "name2", [2.0, 2.0], [[True, True], [True, True]], np.datetime64('2016-12-30'))],
             dtype=recordtype)

print(x[0])
print(x[0]['id'])
print(x[0]['name'])
print(x[0]['grades'])
print(x[0]['grades'][0])
print(x[0]['grades'][1])
print(x[0]['links'])
print(x[0]['links'][0])
print(x[0]['links'][0, 0])
print(x[0]['links'][0, 1])
print(x[0]['links'][1])
print(x[0]['links'][1, 0])
print(x[0]['links'][1, 1])

x[0]['links'][1, 0] = False
x[0]['links'][1, 1] = False
print(x)

print(x[0]['datetime'])

x = np.datetime64('2016-12-30')
print(x)
x = x + np.timedelta64(1)
print(x)


