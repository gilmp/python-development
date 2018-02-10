#!/usr/bin/env python

even_numbers = [2,4,6,8]
odd_numbers  = [1,3,5,7]
allnumbers = odd_numbers + even_numbers
print(allnumbers)
even_numbers = [2,4,6,8]
odd_numbers  = [1,3,5,7]

for x in even_numbers:
    odd_numbers.append(x)
print(len(odd_numbers))
