#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


class AddBookEntry(object):
    """Documentation for AddBookEntry
    """
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print "Created instanse for: ", self.name

    def updatePhone(self, newph):
        self.phone = newph
        print "Updated phone # for: ", self.name


class EmplAddrBookEntry(AddBookEntry):
    """Documentation for EmplAddrBookEntry
    """
    def __init__(self, nm, ph, id, em):
        AddBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em

    def updateEmail(self, newem):
        self.email = newem
        print "Updated email address for: ", self.name
    
