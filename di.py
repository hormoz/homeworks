#50 = 6(5) + 9(0) + 20(1)
#51 = 6(7) + 9(1) + 20(0)
#52 = 6(2) + 9(0) + 20(2)
#53 = 6(4) + 9(1) + 20(1)
#54 = 6(0) + 9(6) + 20(0)
                                               #---- 6*a + 9*b + 20*c = num ----#


#step 1: add 1 to C while C is not equal to Z & equation is not solved;
        #if  C=Z goto step 2

#step 2: add 1 to B while B is not equal to Z & equation is not solved; set C to 0; go the step 1
        #if  B=Z goto step 3

#step 3: add 1 to A while A is not equal to Z & equation is not solved; set C and B to 0; go to step 1
        #if  A=Z -> No Possible Answer

num = 180
z = num/6
a, b, c = 0, 0, 0


while c < num:
    c += 1
    if 9*b + 20*c == num: break

if 9*b + 20*c != num: c = 0


while (b < num) and (9*b + 20*c != num):
    b += 1
    if (9*b + 20*c == num): break
    else:
        while (c < num) and (9*b + 20*c != num):
            c += 1
        if 9*b + 20*c != num: c=0






print num, ("=")
print ("c| 20 *"), c
print ("b| 9 *"), b
