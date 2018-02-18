#!/usr/bin/env python

# The variable that is equal to two, uses an if statement to check if x is equal to 2 if it not not it uses an else method to print out its not equal to two. #

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

# x and y has a defined list containing 1,2,3. There is a method that uses print is x is equal to y then print out true

x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

# Unsure how the not works ##

print(not False) # Prints out True
print((not False) == (False)) # Prints out False
