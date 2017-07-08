#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys


def GetLib():
    FileList = []
    if len(sys.argv) == 1:
        FileList = os.listdir("/home/xiaohai/Software/root/root/lib")
    else:
        FileList = os.listdir(sys.argv[1])
    libList = []
    for var in FileList:
        if os.path.splitext(var)[1] == ".so":
            lib = var.split(".")[0][0]+var.split(".")[0][3:]
            libList.append("-"+lib)
    return libList


if __name__ == '__main__':
    libList = GetLib()
    for i in libList:
        print(i, end=' ')
