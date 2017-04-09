#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    from Tkinter import *
    root = Tk()
    root.title("canvas")
    canvas = Canvas(root, width=400, height=400, bg="blue")
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

    canvas.pack()
    root.mainloop()
