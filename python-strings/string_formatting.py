#/usr/bin/env python

########################################################
# THIS IS ABOUT STRING FORMATTING WITH LISTS OF STRING #
# ... but kinda looks half finished                    #
########################################################

name = "John"
print("Hello, %s!" % name)

name = "John"
age = 23
print("%s is %d years old." % (name, age))

mylist = [1,2,3]
print("A list: %s" % mylist)

#(repr method)

#Basic Arguements 

#%s - String (or any object with a string representation, like numbers)

#%d - Integers

#%f - Floating point numbers

#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

#%x/%X - Integers in hex representation (lowercase/uppercase)

#Defining You Current Balance is $ Unsure why this is used ? 

#Excerise:

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)


