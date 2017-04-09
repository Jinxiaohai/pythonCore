#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import matplotlib.pyplot as plt
import numpy as np


dashes = '\n' + '-'*50
exec_dict = {
    'f': """
    for %s in %s:
        print %s
    """,

    's':"""
    %s = 0
    %s = %s
    while %s < len(%s):
        print %s[%s]
        %s = %s + 1
    """,

    'n':"""
    %s = %d
    while %s < %d:
        print %s
        %s = %s + %d
    """
}

def main():
    ltype = raw_input("Loop type(For/While)?")
    dtype = raw_input("Data type?(Number/Seq)")

    if dtype == 'n':
        start = input('Starting value? ')
        stop = input('Ending value (non-inclusive)? ')
        step = input('Stepping value? ')
        seq = str(range(start, stop, step))

    else:
        seq = raw_input('Enter sequence: ')
        var = raw_input('Iterative variable name ?')

        if ltype == 'f':
            
        
