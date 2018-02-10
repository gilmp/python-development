#!/usr/bin/env python

z = object()
x = object()

x_list = [x] * 20
z_list = [z] * 25
big_list = x_list + z_list

print("x_list contains %d objects" % len(x_list))
print("z_list contains %d objects" % len(z_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 20 and z_list.count(z) == 25:
    print("Almost there...")
if big_list.count(x) == 20 and big_list.count(z) == 10:
    print("Great!")
