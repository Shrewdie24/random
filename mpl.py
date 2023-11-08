#   is a low level graph plotting that serves as a visualization entity in python
#   created by JOHN D. HUNTER
#   it is open source
#written in python, C, Objective-C and java

# example
import matplotlib.pyplot as plt
import numpy as np
# x = np.array([2,10])
# y = np.array([0, 200])
#plt.plot(x,y)
#plt.show()

# x = np.array([1,2,4,7])
# y = np.array(3,12,6,29)
# plt.plot(x,y,'X')
# plt.show()

#USING MARKERS
import matplotlib.pyplot as plt
import numpy as np

y = np.array([1,3,5,2,8,3,12])
plt.plot(y, marker = '4')
plt.show()

# other markers include *,(.),(,),x,X,+,P,s,D,d
# 'o'	Circle	
# '*'	Star	
# '.'	Point	
# ','	Pixel	
# 'x'	X	
# 'X'	X (filled)	
# '+'	Plus	
# 'P'	Plus (filled)	
# 's'	Square	
# 'D'	Diamond	
# 'd'	Diamond (thin)	
# 'p'	Pentagon	
# 'H'	Hexagon	
# 'h'	Hexagon	
# 'v'	Triangle Down	
# '^'	Triangle Up	
# '<'	Triangle Left	
# '>'	Triangle Right	
# '1'	Tri Down	
# '2'	Tri Up	
# '3'	Tri Left	
# '4'	Tri Right	
# '|'	Vline	
# '_'	Hline

#formating strings
import matplotlib.pyplot as plt
import numpy as np
x = np.array([3,8,1,10])
plt.plot(x, '+--r', ms = 12)
plt.show()
#'-'	Solid line
#':'	Dotted line
#'--'	Dashed line
#'-.'	Dashed/dotted line

#COLOR SYNTAX
# 'r'	Red	
# 'g'	Green	
# 'b'	Blue	
# 'c'	Cyan	
# 'm'	Magenta	
# 'y'	Yellow	
# 'k'	Black	
# 'w'	White	

#note that ms IS FOR MARKER SIZE

#SETTING THE EDGE COLOR TO RED
#mec is markeredgecolor
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

#SETTING THE FACE COLOR TO RED
#mfc is markeredgecolor
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

#SETTING THE FACE COLOR AND EDGE COLOR
#NAME OF COLOUR CAN BE IN HEXADECIMAL OR AMONGST THE 140 SUPPORTED COLOR NAMES
#mfc is markeredgecolor
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink',mfc = 'hotpink')
plt.show()
