# Find the length of maximum number of consecutive numbers jumbled up in an array.
# Examples:
# Input : arr[] = {1, 94, 93, 1000, 5, 92, 78};
# Output : 3
# The largest set of consecutive elements is
# 92, 93, 94
#
# Input  : arr[] = {1, 5, 92, 4, 78, 6, 7};
# Output : 4
# The largest set of consecutive elements is
# 4, 5, 6, 7

# This Method will Use Sorting technique to find the Maximum Length of Consecutive Numbers.
# TC : O(NLogN) For Sorting
# SC : O(1)
def maximum_Length_Of_Consecutive_Number_Using_Sorting(arr):
    arr.sort()
    n = len(arr)
    max_length = 1
    current_max = 1
    for i in range(1,n):
        if arr[i] == arr[i-1] + 1 :
            current_max +=1
        else:
            current_max = 1

        # Store the Max Length
        max_length = max(max_length,current_max)

    print("Maximum Length of Consecutive Numbers  {}".format(max_length))


# This Method will use Hashing technique to find maximum length of Consecutive Numbers.
# TC  = O(N)
# SC  = O(N) For Hashing Set
def maximum_Length_Of_Consecutive_Number_Using_Hashing(arr):

    # Initialize the Set & add all elements into the Set.
    S = set()
    for i in arr:
        S.add(i)

    maximum_length = 1
    for i in arr :
        if S.__contains__(i):
            # Check that curr element is the start of the element
            j = i

            # Loop through till the next number is available in set.
            while S.__contains__(j):
                j+=1

            maximum_length = max(maximum_length,j-i)

    print("Maximum Length of Consecutive Numbers  {} ".format(maximum_length))




# Driver Code
arr = [1, 94, 93, 1000, 5, 92, 78]
maximum_Length_Of_Consecutive_Number_Using_Sorting(arr)
maximum_Length_Of_Consecutive_Number_Using_Hashing(arr)
