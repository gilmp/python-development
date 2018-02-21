#!/usr/bin/env python

number = 18
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

# If number which is 18 is greater than 15 print out 1
if number > 15:
    print("1")

# If the first_array has ANY value (ie, it is not empty) print 2 
if first_array:
    print("2")

# Using the len function, if no. of items in list is equal to 2, print 3
if len(second_array) == 2:
    print("3")

# If the added no-of-items in the first and second lists are equal to 5, print 4
if len(first_array) + len(second_array) == 5:
    print("4")

# If the first array IS NOT EMPTY and the first value (0th) in first_array is equal to 1, print 5
if first_array and first_array[0] == 1:
    print("5")

# The NOT operator flips the boolean value over
# second_number is set to 0, and python can treat 0 as False boolean and anything >0 or <0 as True (which is horrible)
# "if 0:" would result as False BUT because of the not, it flips the False into a True
# print 6
if not second_number:
    print("6")

