#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


class HotelRoomCalc(object):
    """Documentation for HotelRoomCalc
    """
    def __init__(self, rt, sales=0.085, rm=0.1):
        self.salesTax = sales
        self.roomTax = rm
        self.rootRate = rt

    def calcTotal(self, days=1):
        daily = round((self.rootRate * (1+self.roomTax + self.salesTax)), 2)
        return float(days) * daily
    
