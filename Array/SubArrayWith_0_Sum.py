# Given an array of positive and negative numbers. Find if there is a sub array (of size at-least one) with 0 sum.
# Input:
# 5
# 4
# 2 - 3
# 1
# 6
# Output:
# Yes
# Explanation:
# 2, -3, 1 is the
# sub array
# with sum 0.


# Approach 1 .
# Find the All Possible Sub array and calculate their sum . If any Of the Sum give 0 then Sub array WIth 0 Sum present.
# TC =  O(N*N) , SC = O(1)

# Approach 2. Better Approach
#   Store the Sum till ith index in a Hashmap . If at any point sum becomes 0 or current sum already exist in our map then it means there is
#   definitely a zero sum sub array exist.      TC = O(N) , SC = O(N)


def isSubarray_With_Zero_Sum_Exist(arr):
    set = {}
    sum = 0
    for i in range(0,len(arr)):
        if arr[i] == 0 or sum+arr[i] in set.keys():
            return True
        else:
            sum = sum+arr[i]
            # If Sum Becomes 0 at any point.
            if sum ==0: return True
            # Else Store the Current Sum in Map
            else: set[sum] = True


    return False

arr = [4,2,-3,1,6]

if isSubarray_With_Zero_Sum_Exist(arr):
    print("Zero Sum Sub array Exist")
else:
    print("Zero Sum sub array does not exist")
