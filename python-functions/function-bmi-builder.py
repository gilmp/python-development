#!/usr/bin/env python

# the gather info function is passing a list of args Height, weight and units and return the values.

heightvalues = ['inches', 'meters']
weightvalues = ['pounds', 'kilograms']

def gather_info():
    unit = raw_input("Are your measurements in metrics or imperial units? ").lower().strip()
    if unit.startswith('i'):
        index=0
    else:
        index=1

    height = float (raw_input("what is your Height in %s ?" % heightvalues[index]))
    weight = float (raw_input("what is your Weight in %s ?" % weightvalues[index]))
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
       
