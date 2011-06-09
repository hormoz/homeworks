# Date: June 9, 2011
# Author: Hormoz Z. Syakal
# Description: A code which prints out prime numbers up to 1000
# Algorithm:
# the way it works ia basicly tries to divide x to y; if the remender is not 0
# it adds up 1 to the y until it is equal to x itself. x will be printed only
# if y is equal to it.
#


print ("2\n3")
x=5
while x < 1000:
    y=3
    while (x%y != 0) and (y <= x):
        y += 1
        if x == y: print x
    x += 2
