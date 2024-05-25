# Author: Kyle Freidhof
# Created: May, 24 2024
# LICENSE: MIT
# Credits: https://www.programiz.com/python-programming/examples/swap-variables
# About: A simple program to swap the varriable

# Defining the function as var for varriable
def var():
    # Ask for two user inputs 
    # So for exampe 5 and 10
    a = input("Enter a value for the varriable a: ")
    b = input("Enter a value for the varriable b: ")

# Assign t as a 
# An then make  varriable a to b 
# An Varriable b to a 
    t = a
    a = b 
    b = t

# An then print the results 
    print(f"The value of a: {a}")
    print(f"The value of b: {b}")

# Execute the function
var()
