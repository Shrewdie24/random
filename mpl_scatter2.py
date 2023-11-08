#combining alpha and sizes

import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x,y, c=colors, s=sizes, alpha=0.5,cmap='prism')
plt.colorbar()
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
# other cmaps include jet,magma,ocean,spectra,wistia,binary,cividis,inferno
