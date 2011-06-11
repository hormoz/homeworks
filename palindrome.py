#
# Descrition: Finds out if a word is palindromic
# Algorithm: it uses recursive loop (@ line 11)
#

def isPalindrome(x):
    x = str(x)
    if len(x)<=1:
        return True
    else:
        return x[0] == x[-1] and isPalindrome(x[1:-1])

a = raw_input("Enter a word: ")

if isPalindrome(a): print("It IS")
if not isPalindrome(a): print("It IS NOT")
