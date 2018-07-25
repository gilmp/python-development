#!/usr/bin/env python

api_calls = raw_input("")
message = raw_input("Please enter the message: ")
count = raw_input("You have processed [1]: " ).strip()

if count:
   count = int(count)
else
    count = 1

def multi_echo(message, count):
    while count > 0:
        print(message)
        count -= 1
multi_echo(message,count)

e