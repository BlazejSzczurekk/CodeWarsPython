# a - first term
# r - common ratio
# n - amount of terms
#solution
def geometric_sequence_sum(a, r, n):
    sum=a
    for x in range(n-1):
        sum+=a*r
        a=a*r
    return sum

#test:
print(geometric_sequence_sum(2,3,5)) #should be 242
print(geometric_sequence_sum(1,1,2)) #should be 2
print(geometric_sequence_sum(2,2,10)) #should be 2046
print(geometric_sequence_sum(21,-2,10)) #should be -341
print(geometric_sequence_sum(1,0.5,10)) #should be 1.998046875