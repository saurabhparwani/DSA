# Problem Statement
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# Input: arr[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
#
# Trap "1 unit" between first 1 and 2, "4 units" between
# first 2 and 3 and "1 unit" between second last 1 and last 2

# Bruteforce Approach :
#   An element can store water only if high bars exist on left & side. The idea
#   is to calculate Maximum height in left side from element & calculate Maximum height in right side.\
#   Then take minimum of both the sides and then subtract the height of current element .
#   Keep doing this for every element in Array and add value in result if value is >0 .
#   Time Complexity of this SOlution will be O(N*N) as we are traversing array in  left & right for each (elemnt)
#   Space Complexity will be O(1).


# Approach 2 . In the Previous Approach we are calculating mas height in left & right for every element that is reducing the efficiency of the Alog.
# In this Algo we will Precompute the max height in left & right side and then use it for calculation.
# In this algo we will traverse array 3 times first for storing max left side , then for max right side , and then 3rd time for Caculating the answer.
# Time Complexity would be O(3N) = O(N) . Space Complexity => O(2N) = O(N).
def maximumWaterStored_Using_Precumputation(arr):

    n = len(arr)
    left_max_arr = [0]*n
    right_max_arr = [0]*n
    left_max = -999999
    right_max = -999999
    result = 0

    # Fill left array
    for i in range(0, n):
        left_max_arr[i] = max(left_max, arr[i])
        if left_max < arr[i]:
            left_max = arr[i]

    # Fill right array

    for i in range(n - 1, -1, -1):
        right_max_arr[i] = max(right_max, arr[i])
        if right_max < arr[i]:
            right_max = arr[i]

    # 3rd Loop to calculate the final Answer
    for i in range(n):
        result += min(left_max_arr[i], right_max_arr[i]) - arr[i]

    return  result

# Approach three using two Pointer Algorithm with O(1) Space and O(N) time .
# The idea is too Keep track of left & right maximum while traversing itself.

def maximumTrappedWater_Using_Two_pointer(arr):

    # Declare initial Variable
    low = 0
    high = len(arr) - 1
    left_max = -99999
    right_max = -99999
    result = 0
    while low <= high:

        # Check that if Left Value is less than or equal to right Value.
        if arr[low] <= arr[high]:
            # Check that current element is greater than left Max.
            if left_max < arr[low]:
                left_max = arr[low]

            # Curr element is less than left Maximum, It means that it can trap Water and
            # there will be definitely  a bar on right side with height equal to or grater to left max.
            else:
                result += left_max - arr[low]  # Add the result in answer

            low+=1  # Increase low Pointer in every Condition

        # Left Value if greater than right Value.
        else:

            # Check that current element is greater than right Max.
            if right_max < arr[high]:
                right_max = arr[high]

            # Curr element is less than right Maximum, It means that it can trap Water and
            # there will be definitely  a bar in left side with height equal to or grater to right max.
            else:
                result +=right_max - arr[high]

            high -=1 # reduce the height in both cases.


    return result

# Driver Code
arr= [7,4,0,9]
print(maximumWaterStored_Using_Precumputation(arr))
print(maximumTrappedWater_Using_Two_pointer(arr))
