#!/usr/bin/env python

# The boolean value uses True or false when the if count is great than or equal to 5 and then breaks out of the loop
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9 i # Need to recap Remainder in ranges 
for x in range(10):
    # Check if x is even
    if x % 4 == 0:
        continue
    print(x)
