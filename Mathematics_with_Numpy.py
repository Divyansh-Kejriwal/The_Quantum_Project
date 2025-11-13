import numpy as np

"""Basic Calculations"""
a = np.array([1,2,3])
add = a+2
print(add) # Output --> [3 4 5]

subtract = a-2
print(subtract) # Output --> [-1  0  1]

multiply = a*2
print(multiply)  # Output --> [2  4  6]

divide = a/2
print(divide) # Output --> [0.5  1.  1.5]

exponential = a**2
print(exponential) # Output --> [1  4  9]

"""Calculations using other array"""
b = np.array([1,1,1])

print(a+b) # Output --> [2,3,4]
print(a-b) # Output --> [0,1,3]
print(a*b) # Output --> [1,2,3]
print(a/b) # Output --> [1.  2.  3.]


"""Linear Algebra"""


