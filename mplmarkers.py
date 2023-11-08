# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([3,5,2,7])

# plt.plot(ypoints, marker = '*', ms = 15, mec = 'r',mfc = 'b')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,8])
y = np.array([2,4,6,8,10,12,14])

#setting font properties for the title and label
font1 = {'family': "serif",'size': 20,'color': 'blue'}
font2 = {'family': 'Georgia','size': 15,'color': 'darkred'}


plt.title('Sport watch counter',fontdict= font1, loc = 'left')
plt.xlabel('Average pulse',fontdict= font2)
plt.ylabel('Calorie Burnage',fontdict= font2)

plt.plot(x,y)

plt.show()
