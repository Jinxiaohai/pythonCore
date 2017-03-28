#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""generate bibdatabase"""


import os


def eachFile(filepath):
    pathDir = os.listdir(filepath)
    try:
        tmpfile = open("temprary.txt", "w")
    except IOError:
        pass
    
    for allFile in pathDir:
        child = os.path.join('%s%s' % (filepath, allFile))
        if "bibtex" in child.split("."):
            tmpfile.writelines(child.decode('gbk') + "\n")
    tmpfile.close()
    
    try:
        fopen = open("temprary.txt", "r")
        database = open("BIBDATABASE.bib", "w")
    except IOError:
        pass
    
    for eachFile in fopen:
        eachFile = eachFile.strip("\n")
        fileContent = open(eachFile, "r")
        for eachLine in fileContent:
            # print eachLine,
            database.writelines(eachLine)
        fileContent.close()
    fopen.close()
    database.close()
    os.unlink("temprary.txt")


if __name__ == '__main__':
    cwd = os.getcwd() + "/"
    eachFile(cwd)
