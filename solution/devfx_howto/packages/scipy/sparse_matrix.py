import scipy as sp
import scipy.sparse
import numpy as np

m = np.matrix([[0, 1, 0, 0, 0, 1, 0, 0],
               [0, 2, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 3, 1, 0, 2],
               [0, 0, 0, 1, 0, 1, 0, 0]])
csr_m = sp.sparse.csr_matrix(m)
print("\nCSR matrix representation:\n{}".format(csr_m))


data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sp.sparse.coo_matrix((data, (row_indices, col_indices)))
print("COO matrix representation:\n{}".format(eye_coo))