#!/usr/bin/env python

# This is defining a list of even numbers and odd numbers and concatenating them together
# allnumbers = 1,2,3,4,5,6,7,8
even_numbers = [2,4,6,8]
odd_numbers  = [1,3,5,7]
allnumbers = odd_numbers + even_numbers
print(allnumbers)

# This is using a for loop to add the even numbers to the end of odd_numbers and print out the length of odd numbers
# len = 8
even_numbers = [2,4,6,8]
odd_numbers  = [1,3,5,7]

for x in even_numbers:
    odd_numbers.append(x)
print(len(odd_numbers))

