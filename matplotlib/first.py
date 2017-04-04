#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import matplotlib.pyplot as plt
from numpy.random import randn

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

plt.plot(randn(50).cumsum(), "k--")
ax1.hist(randn(100), bins=20, color="k", alpha=0.3)
# ax2.scatter(np.)
plt.show()
