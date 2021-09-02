# Given an array of integers nums containing n + 1 integers where
# each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# Approach 1 : Use two loops to find the Occurance of the each character. TC = O(N*N) , SC = O(1)
# Approach 2 : Use hash map  to store the frequency of the array elements. TC = O(N) , SC = O(N)

# Approach 3 : Find the sum of all array elements in one traversal , while doing so maintain a max variable
# as well so this way we can find the value of N. Now we can find the sum of elements 1 to N through
# formula N(N+1)/2 . Calculate this sum & subtract this from sum which we got via array traversal.
# TC = O(N) , SC = O(1)
# This approach may give overflow issue in case if numbers are very big as then sum will also be very large and can give overflow.


# Approach 4 : Using the Cycle finding method which we use in linked list to find the loop.
# This approach resolve the overflow issue. TC = O(N) , SC = O(1)

# Method to find the Duplicate number using cycle finding Algo.
def findRepeatingNumber_CycleApproach(arr):
    n = len(arr)
    # If only 1 element is present in array then we can say that there is no duplicate element.
    if n <= 1:
        return -1

    # Initialize slow & fast ptr.
    slow = arr[0]  # Move 1 step
    fast = arr[arr[0]] # Move 2 step

    # Traverse till we found a cycle.
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]

    fast = 0
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    print("Repeating Number is {}".format(slow))



# Method to find the repeating number using the third approach.
def findRepeatingNumber(arr):
    n = len(arr)
    sum = 0
    maximum_element = -9999999
    for i in arr:
        if i > maximum_element:
            maximum_element = i
        sum += i

    print("Repeating Number is {}".format(sum - ((maximum_element*(maximum_element+1))//2)))


# Driver Method
num = [1,1,2]
findRepeatingNumber(num)
findRepeatingNumber_CycleApproach(num)


# Another Variation of the Problem is that there can be more than 1 numbers which are repeating .
# And the numbers are from 1 to n-1 and total numbers are n.
# https://www.geeksforgeeks.org/duplicates-array-using-o1-extra-space-set-2/
