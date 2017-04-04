#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


class MyClass(object):
    """Documentation for MyClass
    """
    def __init__(self):
        pass
    myVersion = "1.1"
    
    def showMyVersion(self):
        print MyClass.myVersion
    

def main():
    print dir(MyClass)


if __name__ == '__main__':
    main()
