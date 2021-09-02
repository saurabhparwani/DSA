# Largest Sum Contiguous Subarray
# Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.
# Brute force Algo will have time complexity of O(N*N).


# Method to get maximum sum of sub array in a array containing positive & negative elements.
# This Method will return the maximum sum in O(NLogN) time.


def mergeSubArray(arr,l,m,h):

    # Get Maximum sum in left half.
    curr_sm = 0
    left_sum = -100000

    for i in range(m,l-1,-1):
        curr_sm = curr_sm + arr[i]

        if curr_sm > left_sum:  # If current sum is greater than left sum.
            left_sum = curr_sm


    # Get Maximum sum in right half.
    curr_sm = 0
    right_sum = -100000

    for i in range(m+1,h+1):
        curr_sm = curr_sm + arr[i]

        if curr_sm > right_sum:  # If current sum is greater than right sum.
            right_sum = curr_sm


    return max(left_sum+right_sum,left_sum,right_sum)


# This Method will work similar to merge sort . It will detect middle element & then call same method for left half & right half.
# Divide the given array in two halves
# Return the maximum of following three
# Maximum subarray sum in left half (Make a recursive call)
# Maximum subarray sum in right half (Make a recursive call)
# Maximum subarray sum such that the subarray crosses the midpoint
def maximumSumSubarrayUsingDivideAndConquer(arr,l,h):

    # Base Case
    if l==h:
        return arr[l]

    m = (l+(h-1))//2   # Same as (l+h)/2


    return max(maximumSumSubarrayUsingDivideAndConquer(arr,l,m),maximumSumSubarrayUsingDivideAndConquer(arr,m+1,h),
               mergeSubArray(arr, l, m, h))



# Implementation of kadane's Algo to find maximum sum subarray.
# Time Complexity of this method is O(N).
def maximumSumSubarray(arr):

    # Declare Global & curr Maximum
    global_max = arr[0]
    curr_max = arr[0]

    # Just to get the index of the Subarray.
    global_start =0
    global_end =0
    curr_start = 0
    curr_end = 0

    for i in range(1,len(arr)):

        # Check for 1st Condition
        if curr_max+arr[i] < arr[i]:
            curr_max = arr[i]
            curr_start=i
            curr_end=i

        else:
            curr_max = curr_max+arr[i]
            curr_end+=1

        # Update the Global Max & it's Position
        if curr_max > global_max:
            global_max = curr_max
            global_start = curr_start
            global_end = curr_end

    print("Maximum Sub array Found from index {} to index {} ".format(global_start,global_end))

    return  global_max

# Driver Code
# Using Kadane's Algo
input = [-2,1,-3,4,-1,2,1,-5,4]
print(maximumSumSubarray(input))

# Using Divide & Conquer
input_arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maximumSumSubarrayUsingDivideAndConquer(input_arr,0,len(input_arr)-1))