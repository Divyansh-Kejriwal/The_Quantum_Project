import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""BASIC GRAPH"""

x = [0,2,3,4]
y = [0,5,6,7]
a = plt.plot(x,y,label = "random_data")                ## -----> a simple line graph in terms of x and y axes and labels the line as random_data

plt.title("Basic Graph")                ## -----> Shows a title at the top of the graph
plt.xlabel("X-axis") ; plt.ylabel("Y-axis") ## -----> Adds label on x and y axis

plt.xticks([1,2,3,4,5,6,7,8,9,10])          ## -----> The unit of X-axis changes to the give values in this case integer
plt.yticks([1,2,3,4,5,6,7,8,9,10])          ## -----> The unit of Y-axis changes to the give values in this case integer

plt.legend()                                ## -----> puts a legend on the graph

"""Another Line"""

data_1 = np.arange(0,4.5,0.5)
plt.plot(data_1 , data_1**2 ,label = "Parabola", linewidth = 2, linestyle = '--', marker = '.', markeredgecolor = 'red')     ## -----> display properties of line
plt.legend()                                ## -----> Puts legend on the other line

plt.show()                                  ## -----> Used to display a graph
