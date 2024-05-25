# Here is a basic program that does chaotic things 

def main():
    print("A Program that does chaotic things")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(5):
        x = 4.9 * x * (1 - x)
        print(x)


main()
