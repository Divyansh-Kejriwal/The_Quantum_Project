import numpy as np

a = np.array([[1,2,3,4,5,6,7],
              [11,12,13,14,15,16,17]])

"""to get a specific element from a row and a column [r, c]"""
print(a[1, 5]) # index in python starts from 0 output --> 6
print(a[-1, -2]) # also works with negative notations output --> 16

"""to get a specific row or a column"""
print(a[0, :]) # this notation is used for slicing in array output --> [1,2,3,4,5,6,7]
print(a[:,1]) # this notation is used for slicing in array output --> [ 2 12]

"""for getting a particular output [start:end:step]"""
print(a[0, 1:6:1]) # output --> [2,4,5,6]
print(a[:,1:6:1]) # output --> [[ 2  3  4  5  6]   [12 13 14 15 16]]

"""for editing a particular value"""
a[1,5] = 20
print(a) # output --> [[ 1  2  3  4  5  6  7]    [11 12 13 14 15 20 17]]

a[: , 1]=3
print(a) # output --> [[ 1  3  3  4  5  6  7]   [11  3 13 14 15 20 17]]

a[0] = 5
print(a) # output --> [[ 5  5  5  5  5  5  5]    [11 12 13 14 15 20 17]]

"""Accessing elements in a multi-dimensional array"""
b = np.array([[[1,2,3],[4,5,6]],
              [[7,8,9],[10,11,12]]])

print(b[0,1,1]) # in 3D array output --> 5
