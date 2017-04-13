#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys


def hold(linelist):
    for eachline in reversed(linelist):
        if (eachline[5].upper() == 'I'
            and eachline[4] == r'0+00:00:00'):
            commandHold = 'condor_hold ' + str(eachline[0])
            os.system(commandHold)

def release(linelist):
    count = 0
    for eachline in linelist:
        if eachline[5].upper() == 'R' or eachline[5].upper() == 'I':
            count += 1
            
    if count < 50:
        for eachline in linelist:
            if (eachline[5].upper() == 'H'):
                commandRelease = 'condor_release ' + str(eachline[0])
                os.system(commandRelease)
                count += 1
                if count > 50:
                    break

def read(tmpfile='log.txt'):
    linelist = []
    chongdingxiang = 'condor_q jinxiaohai > ' + str(tmpfile)
    os.system(chongdingxiang)
    try:
        if os.path.exists(tmpfile):
            fileobj = open(tmpfile, 'r')
            for eachline in fileobj:
                if len(eachline.strip('\n').split()) == 10:
                    linelist.append(eachline.strip('\n').split())
            fileobj.close()
    except Exception:
        pass
    return linelist


def main():
    linelist1 = read()
    hold(linelist1)
    while True:
        linelist2 = read()
        release(linelist2)
        os.system('sleep 60')


if __name__ == '__main__':
    main()
