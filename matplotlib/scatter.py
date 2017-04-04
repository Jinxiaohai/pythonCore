#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import matplotlib.pyplot as plt
import numpy


fig, axes = subplot(1, 1, 1)
x = numpy.random.randn(1000)
y = numpy.random.randn(1000)
axes.scatter(x, y, color="green")
plt.show()
