# -*- coding: utf-8 -*-
# SVD Sample with Python and NumPy
import numpy as np

# # Target matrix.
# X = np.array([[1,2], [3,4]])
# print("X=\n" + str(X))

# # SVD.
# U, S, V = np.linalg.svd(X, full_matrices=False)
# print("U=\n" + str(U))
# print("S=\n" + str(np.diag(S)))
# print("V=\n" + str(V))

# # Reverse to original matrix.
# X_rev = np.dot(np.dot(U, np.diag(S)) ,V)
# print("X_rev=\n" + str(X_rev))

# # Check Unitary matrix.
# print("Unitary=\n" + str(np.dot(U, U.T)))

# print("\n------------------------\n")

B = np.random.randn(9, 5)
print("B=\n" + str(B))
print("B.shape=", B.shape)

# http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linalg.svd.html
# Reconstruction based on full SVD.
U, s, V = np.linalg.svd(B, full_matrices=True)
print("U/s/V.shape=", U.shape, s.shape, V.shape)
S = np.zeros((U.shape[0], V.shape[0]), dtype=complex)
S[:V.shape[0], :V.shape[0]] = np.diag(s)
print("S.shape=", S.shape) 
B_rev = np.dot(U, np.dot(S, V))
print(B_rev)
print(np.allclose(B, B_rev))

print("\n------------------------\n")

# Reconstruction based on reduced SVD:
U, s, V = np.linalg.svd(B, full_matrices=False)
print("U/s/V.shape=", U.shape, s.shape, V.shape)
S = np.diag(s)
B_rev = np.dot(U, np.dot(S, V))
print(B_rev)
print(np.allclose(B, B_rev))

# >>> U, s, V = np.linalg.svd(a, full_matrices=False)
# >>> U.shape, V.shape, s.shape
# ((9, 6), (6, 6), (6,))
# >>> S = np.diag(s)
# >>> np.allclose(a, np.dot(U, np.dot(S, V)))
# True


print("\n------------------------\n")

# 次元を自分で落とす
U, s, V = np.linalg.svd(B, full_matrices=False)
print("U/s/V.shape=", U.shape, s.shape, V.shape)
print(s)
s[2:] = 0
print(s)
S = np.diag(s)
print(S)
B_rev = np.dot(U, np.dot(S, V))
print(B_rev)
# print(np.allclose(B, B_rev))

# 次元圧縮
# http://d.hatena.ne.jp/a_bicky/20100905/1283660172

# TODO1 1つずつ次元を落として、差分を出してみよう
# TODO2 スパースな方も試してみよう
# TODO3 スパースなやつで、次元を落としてみて、差分を見るのと、ゼロがどれだけ減るかをみてみよう




















































