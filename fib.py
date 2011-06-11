#
# Description: calculates the fibonacci numbers
#

def fib(x):
    if x <= 1: return 1
    else: return fib(x-1) + fib(x-2)

a = raw_input("put a number: ")
a = int(a)
print fib(a)
