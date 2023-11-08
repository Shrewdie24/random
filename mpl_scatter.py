import matplotlib.pyplot as plt
import numpy as np

#Creating Scatter plots
# use the scatter() function
# x = np.array([5,7,8,7,17,2,5,9,5,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,86,85])
# plt.scatter(x,y)
# plt.show()
# you can plot more than one scatter plot, comparing the two plots judges our conclusion

# comparing plots
import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.xlabel('age')
# plt.ylabel('speed')
# plt.scatter(x, y, color = 'green')

#day two, the age and speed of 15 cars:
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.xlabel('age')
# plt.ylabel('speed')
# colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta", "blue","hotpink"])
# plt.scatter(x, y, c = colors)

# plt.show()

#colormap - viridis, 0 is yellow, 100 is purple
import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([100, 90, 80, 70, 60, 55, 50, 45, 40, 30, 20, 10, 0])

plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar() #adding the colormap
plt.show()

#changing the size of the markers
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.scatter(x,y, s = sizes, alpha = 0.5)

plt.show()


#combining alpha and sizes
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x,y, c=colors, s=sizes, alpha=0.5,cmap='nipy_spectral')
plt.colorbar()
plt.show()
