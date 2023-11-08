import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,8])
y = np.array([2,4,6,8,10,22,18])

plt.title('Sports Watch Counter')
plt.xlabel('Average Pulse')
plt.ylabel('Calories Burnage')

plt.plot(x,y)
#plt.grid(axis='y')

#setting line properties for the grid
plt.grid(color = 'green', linestyle = '--', linewidth = 1.0)
plt.show()