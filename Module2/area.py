# Author: Kyle Freidhof
# Created: May, 25 2024
# LICENSE: MIT
# Creditts: https://www.programiz.com/python-programming/examples/area-triangle
# About: A simple program to solve the area of a triangle 

# Defining the function
def main():
    # Ask the user for 3 inputs and store them in the  varriable
    x = eval(input("Enter the first number: "))
    y = eval(input("Enter the second number: "))
    z = eval(input("Enter the third number: "))

    # Solve the permiter stored in the varriable
    a = (x + y + z) / 2

    # Solve the area of the triangle 
    ar = (a*(a-x)*(a-y)*(a-z)) ** 0.5
    # Print out the results
    print("The answer to the area of the triangle is: ", ar)
# Execute the function
main()
