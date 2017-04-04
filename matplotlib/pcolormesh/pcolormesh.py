#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import matplotlib.pyplot as plt
import numpy as np


# Sample data
side = np.linspace(-2, 2, 15)
X,Y = np.meshgrid(side, side)
Z = np.exp(-((X-1)**2+Y**2))

# Plot the density map using nearest-neighbor interpolation
plt.pcolormesh(X, Y, Z)
plt.savefig("pcolormesh.png")
plt.show()
