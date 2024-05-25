# Author: Kyle Freidhof
# Created: May, 25 2024
# License: MIT
# Credits: Python Programing An Introduction to Computer Science Third Edition John Zelle
# About: a Simple Program to convert Fahrenheit to Celsius 
   

# The Main function
def main():
    # Gain input on what the Temperature is 
    faren = eval(input("What is the Ferenheight Temperature: "))
    # Then based on the formula convert it to Celsius 
    cel = ( faren - 32 ) * 5/9  
    # Print The Output
    print("It is", cel, "degrees Celsius")
    # Then Convert it back to Faherenheit
    c = (cel * 9/5) + 32
    print("It is", c, "degress Fahrenheit")
# An Run the function below 
main()
