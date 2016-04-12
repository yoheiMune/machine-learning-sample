# -*- coding: utf-8 -*-
# SVD.
# Identify how many dimentions can we reduce.
import numpy as np


# Target matrix.
A = np.random.randn(160, 90)
# print(A)

# SVD.
U, s, V = np.linalg.svd(A, full_matrices=False)
print("U/s/V.shape=", U.shape, s.shape, V.shape)

# Reverse to original.
S = np.diag(s)
A_rev = np.dot(U, np.dot(S, V))
print(np.allclose(A, A_rev))

# Reduce dimentions step by step.
for i in range(s.shape[0], 0, -1):

    # Reverse to A.
    s_reduce = np.zeros(s.shape[0])
    s_reduce[0:i] = s[0:i]
    S = np.diag(s_reduce)
    A_rev = np.dot(U, np.dot(S, V))

    # Calcurate score.
    diff = sum(sum((A - A_rev) ** 2)) / (A.shape[0] * A.shape[1])
    variance = np.var(A)
    score = diff / variance
    
    # Judge.
    border = 0.01   # hyper parameter.
    if (score <= border):
        print("OK :", i, score, diff, variance)
    else:
        print("NG :", i, score, diff, variance)



if __name__ == "__main__":
    pass