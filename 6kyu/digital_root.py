#Digital root is the recursive sum of all the digits in a number.
#Given n, take the sum of the digits of n. If that value has more than one digit, 
#continue reducing in this way until a single-digit number is produced. 
#The input will be a non-negative integer.

#Examples
#    16  -->  1 + 6 = 7
#   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
#132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
#493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


#solution

def digital_root(n):
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    if sum>=10:
        sum=digital_root(sum)
    return sum

#test

print(digital_root(16)) #should be 7
print(digital_root(942)) #should be 6 
print(digital_root(132189)) #should be 6
print(digital_root(493193)) #should be 2