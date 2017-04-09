#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import subprocess
import matplotlib.pyplot as plt
import numpy as np


fileobj = open("./ampt/ana/ampt.dat")
multi = int(fileobj.readline().strip('\n').split()[2])

xlist = []
ylist = []

for i in range(multi):
    eachline = fileobj.readline().strip('\n').split()
    x = float(eachline[5])
    y = float(eachline[6])
    if abs(x) < 15 and abs(y) < 15:
        xlist.append(x)
        ylist.append(y)

plt.scatter(xlist, ylist)
plt.show()
