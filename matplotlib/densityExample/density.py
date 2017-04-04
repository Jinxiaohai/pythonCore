#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import LogNorm


x, y, z = np.loadtxt('data.txt', unpack=True)
N = int(len(z)**.5)
z = z.reshape(N, N)
plt.imshow(z+10, extent=(np.amin(x), np.amax(x), np.amin(y), np.amax(y)),
           cmap=cm.hot, norm=LogNorm())
plt.colorbar()
plt.show()
