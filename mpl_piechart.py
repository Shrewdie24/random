# import matplotlib.pyplot as plt
# import numpy as np

# y = np.array([35,25,15,26,14,25,45])
# mylabels = ['Apples','Bananas','Cherries','Dates','Guava','Kiwi','Mango']
# plt.pie(y, labels= mylabels, startangle = 90)
# plt.show()

#use the explode parameter to allow the wedges stand out
import matplotlib.pyplot as plt 
import numpy as np

y = np.array([35,25,15,26,14,25])
mylabels = ['Apples','Bananas','Cherries','Dates','Tangerines','Guavas']
myexplode = [0,0.2,0,0,0,0.2]

plt.pie(y, labels = mylabels, explode = myexplode, shadow=True)
plt.show()
#add shadow using shadow attribute,you can select colors like a dict e.g mylabels   
# to add a list of explanation for each wedge, use the legend()function
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
mylabels = ['Apples','Bananas','Cherries','Dates']

plt.pie(y, labels = mylabels)
plt.legend()
plt.show()