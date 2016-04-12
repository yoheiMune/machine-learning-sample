# -*- coding: utf-8 -*-
# SVD for sparse data.
import random
import numpy as np
from scipy.sparse.linalg import svds


# Target matrix.
A = np.zeros((1000, 1000))

# Add some data for creating sparse situation.
for i in range(50000):
    try:
        row = random.randint(0, 999)
        col = random.randint(0, 999)
        A[row, col] = 1
    except:
        print(row, col)

# How sparse.
sparse_raito = 1 - A[A!=0].shape[0] / 1000 / 1000
print("sparse: %.2f%%" % (sparse_raito * 100))


# SVD for sparse
U, s, V = svds(A)
# print(U)
# print(s)
# print(V)


# Reverse.
S = np.diag(s)
A_rev = np.dot(U, np.dot(S, V))

# How sparse.
sparse_raito = 1 - A_rev[A_rev!=0].shape[0] / 1000 / 1000
print("sparse: %.2f%%" % (sparse_raito * 100))




































































