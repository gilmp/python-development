#!/usr/bin/env python

# Strings can be in double quotes
string1 = "Hello World!"
print(string1)

# Strings can be in single quotes
string2 = 'Hello world!'
print(string2)

# You can store Strings in variables or use them in place
string1 = "print my string variable"
print(string1)
print("print my string literal")

# You can concatinate strings together with the + operator
string1 = "1st string"
string2 = "2nd string"
string3 = string1 + " " + string2
print(string3)

# If you want a single quote as part of your string
# you can define your string in double quotes and visa versa
string1 = "Don't shoot the messenger"
string2 = '"I hope you know whats going on here" he said'
print(string1)
print(string2)

# You can get the length of a string with the 'len' function
string1 = "this string is 33 characters long"
print(len(string1))

# You can find the 1st indexed position of a character with the String method 'index'
string1 = "Hello world!"
print(string1.index("o"))

# You can count how many occurances of a character exist with the Strng method 'count'
astring = "Hello world!"
print(astring.count("l"))

