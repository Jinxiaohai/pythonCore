#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
from pylab import *


x = np.random.randn(100000)
y = np.random.randn(100000)
plt.hist2d(x, y, bins=40, norm=LogNorm())

plt.colorbar()
plt.savefig("hist2d.png")
