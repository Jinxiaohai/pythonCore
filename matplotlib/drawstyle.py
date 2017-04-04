#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import matplotlib.pyplot as plt
import numpy


plt.plot(numpy.random.randn(30).cumsum(), color="g", linestyle="dashed", marker="o")
plt.show()
