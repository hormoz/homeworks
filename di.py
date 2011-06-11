# PROBLEM:
#
# Show that it is possible to buy exactly 50, 51, 52, 53, 54, and 55 McNuggets, by finding
# solutions to the Diophantine equation. You can solve this in your head, using paper and pencil,
# or writing a program. However you chose to solve this problem, list the combinations of 6, 9
# and 20 packs of McNuggets you need to buy in order to get each of the exact amounts.
# Given that it is possible to buy sets of 50, 51, 52, 53, 54 or 55 McNuggets by combinations of 6,
# 9 and 20 packs, show that it is possible to buy 56, 57,..., 65 McNuggets. In other words, show
# how, given solutions for 50-55, one can derive solutions for 56-65.

#---- 6*a + 9*b + 20*c = num ----#

#step 1: add 1 to C while C is not equal to Z & equation is not solved;
        #if  C=Z goto step 2

#step 2: add 1 to B while B is not equal to Z & equation is not solved; set C to 0; go the step 1
        #if  B=Z goto step 3

#step 3: add 1 to A while A is not equal to Z & equation is not solved; set C and B to 0; go to step 1
        #if  A=Z -> No Possible Answer

num = input("enter a number: ")
num = int(num)
a, b, c = 0, 0, 0

# a=0 b=0 c=counting
while c < num:
    c += 1
    if 6*a + 9*b + 20*c == num: break

if 6*a + 9*b + 20*c != num: c = 0 # reseting value of c to 0

# a=0 b=counting c=counting
while (b < num) and (6*a + 9*b + 20*c != num):
    b += 1
    if (6*a + 9*b + 20*c == num): break
    else:
        while (c < num) and (6*a + 9*b + 20*c != num):
            c += 1
        if 6*a + 9*b + 20*c != num: c=0

if 6*a + 9*b + 20*c != num: b, c = 0, 0 # reseting value of b & c to 0

# a=counting b=counting c=counting
while (a < num) and (6*a + 9*b + 20*c != num):
    a += 1
    if 6*a + 9*b + 20*c == num: break
    else:
        while (b < num) and (6*a + 9*b + 20*c != num):
            b += 1
            if (6*a + 9*b + 20*c == num): break
            else:
                while (c < num) and (6*a + 9*b + 20*c != num):
                    c += 1
            if 6*a + 9*b + 20*c != num: c=0
    if 6*a + 9*b + 20*c != num: b=0




print (), num
print ("c| 20 *"), c
print ("b| 9 *"), b
print ("a| 6 *"), a

# KNOWN BUG: put 52, feelin' sleepy right now.
