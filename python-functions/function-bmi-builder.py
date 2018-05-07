#!/usr/bin/env python

# the gather info function is passing a list of args Height, weight and units and return the values.
def gather_info():
    height = float (raw_input("what is your Height? (inches or meters) "))
    weight = float (raw_input("what is your Weight? (pounds or kilograms) "))
    unit = raw_input("Are your measurements in metrics or imperial units? ").lower().strip()
    return (height, weight, unit)

# The calculate bmi functions is passing arguements and checking what letter is entered by the user the typed characher i or m,  will then do a calulation within the if statements. and print the bmi.  
def calculate_bmi(weight, height, unit='metric'):
    if unit.startswith('i'):
       bmi = convert_unit_imperial(weight, height)
    elif unit.startswith('m'):
       bmi = convert_unit_metric(weight, height)
    print(" Your bmi is %s" % bmi)

def convert_unit_imperial(weight, height):
    return 703 * (weight / (height ** 2))

def convert_unit_metric(weight, height):
    return (weight / (height ** 2 ))

while True:
    height, weight, unit = gather_info()
    if unit.startswith('i'):
        calculate_bmi(weight=weight, unit='imperial', height=height)
        break
    elif unit.startswith('m'):
        calculate_bmi(weight, height)
        break
    else:
        print("Error: Unknown input. Please use Imperial or metric.")
       
