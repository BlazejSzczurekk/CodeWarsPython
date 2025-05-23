#Find the sum of the odd numbers within an array, after cubing the initial integers. The function should return undefined/None/nil/NULL if any of the values aren't numbers.

#solution

def cube_odd(arr):
    sum=0
    for x in arr:
        if not isinstance(x,int) or isinstance(x,bool):
            return None
        else:
            if x%2!=0:
                sum += x**3
    
    return sum

#test:
print(cube_odd([1, 2, 3, 4])) #should be 28
print(cube_odd([-3, -2, 2, 3])) #should be 0
print(cube_odd(["a", 12, 9, "z",42])) #should be none
print(cube_odd([True, False, 2, 4, 1])) #should be none