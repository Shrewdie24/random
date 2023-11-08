import matplotlib.pyplot as plt
import numpy as np

#plot1
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,3,1)
plt.title('SALES')
plt.plot(x,y)

#plot2
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,2)
plt.title('PURCHASES')
plt.plot(x,y)

#plot3
x = np.array([0,1,2,3])
y = np.array([2,3,5,7])
plt.subplot(2,3,3)
plt.title('EXPENDITURES')
plt.plot(x,y)

#plot4
x = np.array([0,1,2,3])
y = np.array([7,11,13,17])
plt.subplot(2,3,4)
plt.title('GROSS PROFIT')
plt.plot(x,y)

#plot5
x = np.array([0,1,2,3])
y = np.array([0,1,4,9])
plt.subplot(2,3,5)
plt.title('SHORTAGE')
plt.plot(x,y)

#plot6
x = np.array([0,1,2,3])
y = np.array([1,1,2,3])
plt.subplot(2,3,6)
plt.title('NETPROFIT')
plt.plot(x,y)

plt.suptitle('My Business')
plt.show()