#!/usr/bin/env python

# Define functions this function with print the lital string
def my_function():
    print("Hello From My Function!")


# This function will define a function with arguement token replace sting into the print method.
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

# This function is defining to values a,b which is being called 1,2 and then returning the addition of the values.
def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
