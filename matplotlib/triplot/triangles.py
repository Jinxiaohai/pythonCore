#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import matplotlib.pyplot as plt
import numpy as np


x = np.random.randn(100)
y = np.random.randn(100)

plt.triplot(x, y, marker='o', color="red")
plt.show()
