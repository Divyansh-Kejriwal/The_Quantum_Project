import numpy as np

""""
Why do we use Numpy over Lists:
1. it stores a fixed value directly unlike lists which use multiple factors
2. it uses less memory as compared to lists faster to read and retrieve
3. no type checking when iterating through objects
4. it stores data together unlike lists which scatter it all around in the memory
5. better cache utilization and can perform same operations on different data
6. it can do more than lists
"""

a = np.array([1,2,3]) # it creates a 1D array
b= np.array([[4,5,6],[7,8,9]]) # it creates a 2D array

"""to get the dimensions of the created arrays ndim-(no, of dimensions) """

print(a.ndim) # output --> 1
print(b.ndim)# output --> 2

"""to get the shape of the arrays (gives out the result in a grid manner)"""

print(a.shape) # output --> (3,) 3 rows and 0 column
print(b.shape) # output --> (2,3) 2 rows and 3 column

"""to get the data type of an array dtype-(type of data)"""

print(a.dtype) # output --> int64
print(b.dtype) # output --> int64

"""to get the size of an array"""
print(a.itemsize) # output --> 8 byte
print(b.itemsize) # output --> 8 byte

"""to get the total size of an array (can also be the no. of elements)"""

print(a.size) # output --> 3
print(b.size) # output --> 6

"""how to change the dtype in an array"""

c = np.array([1.0,2.0,3.0], dtype="int32")
print(c.dtype)
