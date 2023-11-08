# MATPLOTIB SUBPLOT
# this helps to distribute many plots in one figure
import numpy as np
import matplotlib.pyplot as plt

#plot1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(2,1,1)
plt.plot(x,y)

#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,40,80])

plt.subplot(2,1,2)
plt.plot(x,y)

plt.show()  

#the subplot() function takes 3args
#(1,2,1) means 1 row,2 cols,and 1st plot
#(1,2,2) means 1 row,2 cols,and 2nd plot

#If the plots are on each other, then use (2,1,1) and (2,1,2)
