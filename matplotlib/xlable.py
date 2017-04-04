#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import matplotlib.pyplot as plt
import numpy


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(numpy.random.randn(1000).cumsum(), marker='o')
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],
                            rotation=30, fontsize='small')
ax.set_title("my first matplotlib plot")
ax.text(500, 0, "comment", fontsize=12)
ax.legend(['matplotlib'])

plt.show()
