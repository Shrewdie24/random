import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A','B','C','D'])
y = np.array([6,4,8,10])
plt.bar(x,y, color="tomato", width= 0.2) #barh() for horizontal and arg height
plt.show()

