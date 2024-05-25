# Author: Kyle Freidhof
# Created: May, 25 2024
# LICENSE: MIT
# Credits: https://www.programiz.com/python-programming/examples/km-mile
# About: A simple program to convert Kilometers to miles

# Function Defined
def convert():
    # A Varriable to convert kilometers to miles based on what the user input is 
    kil = float(input("Enter kilometers: "))
    # Conversion factor stored in the varriable 
    conv = 0.621371
    # Calcualte the miles and print the results.
    miles = kil * conv
    print("converted into miles:", miles)
    print("From kilometers", kil)

# Execute the function
convert()
