#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


class Time60(object):
    """Documentation for Time60
    """
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min

    def __str__(self):
        return ('%d:%d' % (self.hr, self.min))

    __repr__ = __str__

    def __add(self, other):
        return self.__class__(self.hr + other.hr, self.min + other.min)

    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self
    
