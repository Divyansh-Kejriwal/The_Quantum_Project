import numpy as np

"""All zeroes matrix"""

a = np.zeros((2,3,4,5))
print(a)

""" 'output'
[[[[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]

  [[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]

  [[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]]


 [[[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]

  [[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]

  [[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]]]"""

"""All ones Matrix"""

b = np.ones((2,3))
print(b)  # output --> [[1. 1. 1.] [1. 1. 1.]]

"""For any other number ((size) , no.)"""
c = np.full((2,2), 69)
print(c) # output --> [[69 69]   [69 69]]

"""for more types of arrays -- https://numpy.org/doc/stable/reference/routines.array-creation.html"""

"""For creating a array of same shape"""
d = np.full_like(b, 45)
print(d) # output --> [[45. 45. 45.]    [45. 45. 45.]]

"""Array of random float point (only rows and columns are to be directly specified)"""
e = np.random.rand(4,2,3)
print(e)

"""Array of random integer values"""
f = np.random.randint(0,100,(3,3))
print(f)

"""identity matrix"""
g = np.identity(5)
print(g)

"""For repetition in array"""
h = np.array([[1,2,3]])
h_ = np.repeat(h,3, 0)
print(h_)

"""1	1	1	1	1

   1	0	0	0	1

   1	0	9	0	1

   1	0	0	0	1

   1	1	1	1	1"""

a1 = np.ones((5,5))
a2 = np.zeros((3,3))
a2[1,1]=9
a1[1:4,1:4]=a2
print(a1)

"""Copying an Array"""
i = np.array([1,2,3])
i_ = np.copy(i)
i_[0]=100
print(i_) # output --> [100,2,3] it changes only for i_ not for i
