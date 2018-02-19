#!/usr/bin/env python

# This is defining a list of even number and odd numbers and cancatinating them together. 1,2,3,4,5,6,7,8 #
even_numbers = [2,4,6,8]
odd_numbers  = [1,3,5,7]
allnumbers = odd_numbers + even_numbers
print(allnumbers)
even_numbers = [2,4,6,8]
odd_numbers  = [1,3,5,7]

# This is using a for loop to append even numbers to the end of odd numbers and print out the length of odd numbers# 
for x in even_numbers:
    odd_numbers.append(x)
print(len(odd_numbers))
