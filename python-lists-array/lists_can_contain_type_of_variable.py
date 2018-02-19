#!/usr/bin/env python

# This is how to define a list and and use the append method to add 1,2,3 to the bottom of the file.
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
#print(mylist[0]) # prints 1
#print(mylist[1]) # prints 2
#print(mylist[2]) # prints 3

# This is using a for loop in x using mylist and prints out x which is 1 with a cancatanated string which is number #

for x in mylist:
    print(str( x) +" number")
