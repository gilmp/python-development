#!/usr/bin/env python

########################################################
# THIS IS ABOUT STRING FORMATTING WITH DIFFERENT TYPES #
########################################################

# change this code
mystring = "hello"
myfloat = 10.01
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % myfloat)
if isinstance(myfloat, float) and myfloat == 10.01:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

