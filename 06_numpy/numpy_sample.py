# -*- coding: utf-8 -*-
# Sample of Numpy, Scypy and Matplotlib
# http://cs231n.github.io/python-numpy-tutorial/
import numpy as np

### Array

# Basic.
a = np.array([1,2,3])
print(a)
print(type(a))
print(a.shape)
print(a[0], a[1], a[2])

b = np.array([[1,2,3], [4,5,6]])
print(b)
print(type(b))
print(b.shape)
print(b[0,0], b[0,1], b[1,1])


# Create array utilities.
a = np.zeros((2,2))
print(a)
b = np.ones((1,2))
print(b)
c = np.full((2,2), 7)
print(c)
d = np.eye(2)
print(d)
e = np.random.random((2,2))
print(e)


# Array Indexing.
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = a[:2, 1:3]
print(b)
# "b" just points the memory that "a" has also points.
print(a[0,1])
b[0,0] = 7
print(a[0,1])

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row_r1 = a[1,:] # Rank1
print(row_r1)
print(row_r1.shape)
row_r2 = a[1:2,:] # Rank2
print(row_r2)
print(row_r2.shape)
col_r1 = a[:,1]
print(col_r1, col_r1.shape)
col_r2 = a[:,1:2]
print(col_r2, col_r2.shape)

# Integer array indexing.
a = np.array([[1,2], [3,4], [5,6]])
print(a[[0,1,2], [0,1,0]])
print(np.array([a[0,0], a[1,1], a[2,0]])) # same above.

a = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
b = np.array([0,2,0,1])
print(a[np.arange(4), b])

a[np.arange(4), b] += 10
print(a)

# Boolean array indexing.
a = np.array([[1,2], [3,4], [5,6]])
bool_idx = (a > 2)
print(bool_idx)
print(a[bool_idx])
print(a[a > 2])

# Data type.
a = np.array([1,2])
print(a.dtype)
b = np.array([1.0,2.0])
print(b.dtype)
c = np.array([1,2], dtype=np.uint8)
print(c.dtype)


## Array math.
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
# element-wise.
print(a + b)
print(np.add(a,b))
print(a - b)
print(np.subtract(a,b))
print(a * b)
print(np.multiply(a,b))
print(a / b)
print(np.divide(a,b))
print(np.sqrt(a))

x = np.array([[1,2], [3,4]])
y = np.array([[5,6], [7,8]])
v = np.array([9,10])
w = np.array([11,12])
# inenr poduct.
print(v.dot(w))
print(np.dot(v, w))
# matrix - vector product.
print(x.dot(w))
print(np.dot(x, w))
# matrix - matrix product.
print(x.dot(y))
print(np.dot(x, y))

# sum.
x = np.array([[1,2], [3,4]])
print(np.sum(x))
print(np.sum(x, axis=0)) # compute sum of each column.
print(np.sum(x, axis=1)) # compute sum of each row.

# transpose.
x = np.array([[1,2], [3,4]])
print(x.T)
v = np.array([1,2,3])
print(v.T) # taking the transpose of rank1(vector) does nothing.


## Broadcasting
#1: Using explicit loop.
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
v = np.array([1,0,1])
y = np.empty_like(x) # Create an empty matrix with the same shape as "x"
for i in range(4):
    y[i,:] = x[i,:] + v
print(y)
#2: Using a vector with the same dimension.
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
v = np.array([1,0,1])
y = np.empty_like(x)
vv = np.tile(v, (4,1))
y = x + vv
print(y)
#3: Using broadcasting.
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
v = np.array([1,0,1])
y = x + v
print(y)

# vector - vector outer product.
v = np.array([1,2,3])
w = np.array([4,5])
print(np.reshape(v, (3,1)) * w) # 3 by 2

# Add a vector to each row.
x = np.array([[1,2,3], [4,5,6]])
v = np.array([1,2,3])
print(x + v)

# Add a vetor to each column.
x = np.array([[1,2,3], [4,5,6]])
w = np.array([4,5])
print((x.T + w).T)

# Another solution.
print(x + np.reshape(w, (2,1)))

# Multiply a matrix by a constant.
x = np.array([[1,2,3], [4,5,6]])
print(x * 2)


