#!/usr/bin/env python


# Using these value inside an list, and an variable the following must equal to true for all if statements.
# change this code
number = 18
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

# If number which is 18 is greater than 15 print out 1
if number > 15:
    print("1")


# If the first_array has the number 2 print 2 
if first_array:
    print("2")

# if the len method of the second array is counts 2 values in the arrary then print 3
if len(second_array) == 2:
    print("3")

# if the len operator is 123 and second array is 1,2 added together to equal 5 print 4
if len(first_array) + len(second_array) == 5:
    print("4")

# if the first array and first array is index is equal to 0 it should equal to 1 in the array
if first_array and first_array[0] == 1:
    print("5")
# if the second number is not ( unsure of this one
if not second_number:
    print("6")
