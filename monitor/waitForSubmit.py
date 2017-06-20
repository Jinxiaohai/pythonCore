#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys


def submit(linelist):
    commandSubmit = 'condor_submit ' + str(epsilon.con)
    reverseList = reversed(linelist)
    if int(reverseList[0][0]) < 10000:
        os.system(commandSubmit)
        os._exit()


def read(tmpfile='log.txt'):
    linelist = []
    chongdingxiang = 'condor_q > ' + str(tmpfile)
    os.system(chongdingxiang)
    try:
        if os.path.exists(tmpfile):
            fileobj = open(tmpfile, 'r')
            for eachline in fileobj:
                linelist.append(eachline.strip('\n').split())
            fileobj.close()
    except Exception:
        pass
    return linelist


def main():
    # linelist1 = read()
    # hold(linelist1)
    while True:
        linelist2 = read()
        submit(linelist2)
        os.system('sleep 30')


if __name__ == '__main__':
    main()
