#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""q"""


import os
import sys
import matplotlib.pyplot as plt
import numpy as np


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.scatter(x, y, s=area, c=colors)
plt.savefig("scatter.png")
plt.show()
