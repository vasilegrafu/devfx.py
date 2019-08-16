import itertools as it

v = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

v_iter = iter(v)

v_slice = list(it.islice(v_iter, 3))
print(v_slice)

v_slice = list(it.islice(v_iter, 3))
print(v_slice)

v_slice = list(it.islice(v_iter, 3))
print(v_slice)

v_slice = list(it.islice(v_iter, 3))
print(v_slice)

v_slice = list(it.islice(v_iter, 3))
print(v_slice)
