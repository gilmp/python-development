#!/usr/bin/env python

# The 'and' operator checks that BOTH conditions are True. Only then will it print
# name == "John" is True, age = 23 is True, therefor print 

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old. ")

# The 'or' operator checks that AT LEAST ONE (can be more) condition is True. Only then will it print
# name == "John" is True, name == "Rick" is False, therefor print 

if name == "John" or name == "Rick":
    print("Your name is either John or Ricki.")

