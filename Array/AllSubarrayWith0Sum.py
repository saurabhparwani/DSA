# Problem Statement : https://practice.geeksforgeeks.org/problems/zero-sum-subarrays1825/1
# Youtube Solution  : https://www.youtube.com/watch?v=C9-n_H7dsvU


# Method 1 : Generate all the sub arrays and count all the zero sum subarray.


# Method 2 : Using Hash map
#  1. Initialize the hash map with initial sum 0 with frequency 1.
#  2. Calculate the sum of element till the current index and check .
#      1. If sum is already not exist in the hash map then insert sum with frequency 1.
#      2. If sum is already exist then increase the count


def countSubArrayWith0Sum(arr):

    sum = 0
    count = 0
    hash_map = {}

    # Store the 0 Sum in the hash map with frequency 1.
    hash_map[0] = 1

    for i in arr:

        sum = sum + i

        # If sum is already present in hash_map.
        # Add the frequency of the sum to the count variable & increase the frequency of the sum by 1.
        if sum in hash_map:
            count  = count + hash_map[sum]
            hash_map[sum] = hash_map[sum] + 1

        else:
            hash_map[sum] = 1

    return count

# Driver Code

arr1 = [0,0,5,5,0,0]
arr2 = [6,-1,-3,4,-2,2,4,6,-12,-7]

print("Count of sub array with zero sum is {}".format(countSubArrayWith0Sum(arr1)))
print("Count of sub array with zero sum is {}".format(countSubArrayWith0Sum(arr2)))
