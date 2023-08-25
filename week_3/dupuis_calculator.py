#-----------------------------------------
# Title: dupuis_calculator.py
# Author: Jocelyn Dupuis
# Date: 08/24/2023
# Description: Python mathematic calculator
#-----------------------------------------

# Function declared to add parameters
def add(x, y):
    # Returns sum 
    return x + y

# Function declared to subtract parameters
def subtract(x, y):
    # Returns difference
    return x - y

# Function declared to divide parameters
def divide(x, y):
    # Returns quotient 
    return x / y

# Function declared to multiply parameters
def multiply(x, y):
    # Returns product
    return x * y

# Variables declared to test calculations
num1 = 13
num2 = 7

# Calls each function passing the variables to create string concatenation
add_result = str(num1) + " + " + str(num2) + " is " + str(add(num1, num2))
subtract_result = str(num1) + " - " + str(num2) + " is " + str(subtract(num1, num2))
divide_result = str(num1) + " / " + str(num2) + " is " + str(divide(num1, num2))
multiply_result = str(num1) + " x " + str(num2) + " is " + str(multiply(num1, num2))

# Prints calculation results 
print(add_result)
print(subtract_result)
print(multiply_result)
print(divide_result)
