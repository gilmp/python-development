#!/usr/bin/env python

# This is defining 2 variables which are defined as a objects in a list #
z = object()
x = object()

# These variable are multipying by 20 and 25 and concaternating them together #
x_list = [x] * 20
z_list = [z] * 25
big_list = x_list + z_list


# This is print the list of variables and using token replace of a decieal and defineing the length of each variable. 
print("x_list contains %d objects" % len(x_list))
print("z_list contains %d objects" % len(z_list))
print("big_list contains %d objects" % len(big_list))

# This is a if statement where xlist is counting how many x is equal to 20 and z list is equal to 225
if x_list.count(x) == 20 and z_list.count(z) == 25:
    print("Almost there...")

# This if statement is big_list is counts x is equal to 20 and z list is equal to 10 and print "Great"
if big_list.count(x) == 20 and big_list.count(z) == 10:
    print("Great!")
