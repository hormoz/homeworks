#
# Description: calculates the square root of a number
#

def sqrt(x):
    if x>0:
        y = 2
        while x/y != y:
            y += 1
        if x/y == y: print y
    else: print("enter a positive number next time")

number = input("Enter a number: ")
sqrt(number)

