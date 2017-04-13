#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""calculate the eccentricity"""


import os
import sys
import math


class Particle(object):
    """Documentation for Particle
    """
    def __init__(self, x, y, z):
        """
        三坐标
        """
        self.x = x
        self.y = y
        self.z = z

    def GetPhi(self):
        return math.atan2(self.y, self.x)

    def GetR2(self):
        return self.x*self.x + self.y+self.y


def GetEccentricity(numerator1, numerator2, denominator):
    numerator = math.sqrt(numerator1*numerator1 + numerator2*numerator2)
    return numerator/denominator

    

def DealWithData(fileobj):
    writeobj = open('epsilon.txt', 'w')
    while True:
        partP = []
        partT = []
        line = fileobj.readline()
        if not line:
            break
        head = line.strip('\n').split()
        multipartP = int(head[2])
        multipartT = int(head[3])
        # print multipartP + multipartT
        for track in range(multipartP+multipartT):
            linelist = fileobj.readline().strip('\n').split()
            # print linelist[2], linelist[3]
            if int(linelist[2]) > 0 and int(linelist[3]) == 3:
                partP.append(Particle(float(linelist[0]),
                                      float(linelist[1]), float(linelist[4])))
            if int(linelist[2]) < 0 and int(linelist[3]) == 3:
                partT.append(Particle(float(linelist[0]),
                                      float(linelist[1]), float(linelist[4])))
        x_cm = 0.
        y_cm = 0.
        count = 0
        for i in partP:
            x_cm += i.x
            y_cm += i.y
            count += 1
            print count
        for j in partT:
            x_cm += j.x
            y_cm += j.y
            count += 1
        x_cm = x_cm/count
        y_cm = y_cm/count
        for i in partP:
            i.x = i.x - x_cm
            i.y = i.y - y_cm
        for j in partT:
            j.x = j.x - x_cm
            j.y = j.y - y_cm
        qx_2 = 0.
        qy_2 = 0.
        qx_3 = 0.
        qy_3 = 0.
        rSquare = 0.
        Count = 0
        for i in partP:
            R2 = i.GetR2()
            phi = i.GetPhi()
            rSquare += R2
            qx_2 += R2 * math.cos(2.*phi)
            qy_2 += R2 * math.sin(2.*phi)
            qx_3 += R2 * math.cos(3.*phi)
            qy_3 += R2 * math.sin(3.*phi)
            Count += 1
        for j in partT:
            R2 = j.GetR2()
            phi = j.GetPhi()
            rSquare += R2
            qx_2 += R2 * math.cos(2.*phi)
            qy_2 += R2 * math.sin(2.*phi)
            qx_3 += R2 * math.cos(3.*phi)
            qy_3 += R2 * math.sin(3.*phi)
            Count += 1
        qx_2 = qx_2/count
        qy_2 = qy_2/count
        qx_3 = qx_3/count
        qy_3 = qy_3/count
        rSquare  = rSquare/count
        epsilon2 = GetEccentricity(qx_2, qy_2, rSquare)
        epsilon3 = GetEccentricity(qx_3, qy_3, rSquare)
        writeobj.write(str(epsilon2))
        writeobj.write("      ")
        writeobj.write(str(epsilon3))
    writeobj.close()


def main():
    fileobj = open('./npart-xy.dat','r')
    DealWithData(fileobj)
    fileobj.close()

if __name__ == '__main__':
    main()
