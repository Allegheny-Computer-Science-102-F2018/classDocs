#!/usr/bin/env python3

#date: 31 Oct 2018
# simple Class demo

class SimpleBooks:
    """The SimpleBooks class: allows to store author name and book title"""
    def __init__(self, author, title):
        print("  Hello! Class SimpleBooks __init__ method()")
        self.author = author
        self.title = title
    #end of __init__()
    def toString(self):
        """method to return author and title"""
        print("  The author : ",self.author)
        print("  The title  : ",self.title)
    # end of toString()

# end of SimpleBooks class

#################################################
# inialize the class and push parameters to class
#################################################


title = "My own AMAZING LIFE! HA HA HA HA"
author = "Sir Edward William The Third"

myBook = SimpleBooks(title, author)
myBook.toString()


title = "The Hardy Boys"
author = "Franklin W Dixon"

myBook1 = SimpleBooks(title, author)
myBook1.toString()
