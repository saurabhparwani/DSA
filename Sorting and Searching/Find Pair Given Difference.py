# Problem Statement
# Given an array Arr[] of size L and a number N,
# You need to write a program to find if there exists a pair of elements in the array whose difference is N.
# Input:
# L = 6, N = 78
# arr[] = {5, 20, 3, 2, 5, 80}
# Output: 1
# Explanation: (2, 80) have difference of 78.

# Input:
# L = 5, N = 45
# arr[] = {90, 70, 20, 80, 50}
# Output: -1
# Explanation: There is no pair with difference of 45.

# Approach 1 find all pair in the array by using two loops but that will take  O(N*N) time .

# Approach 2 using hash map traverse the array and check if the element is already exist in map or not .
# If it is already exist then Pair exist else add the current number with given diff element and store that in map as key.
# If the complete array traversal done and he don't find any element that exist already then return False.
# TC : O(N)  # SC : O(N)

def findPairGivenDiff(arr,L,N):

    hash_map = {}
    for i in range(L):
        hash_map[arr[i]] = i
    for i in range(L):
        if arr[i]+N in hash_map:
            return True
    return False


# Approach 3 use Sorting . First sort the array in Ascending order and then select first element and look for another element in sorted array.

def findPairWithGivenDiff_UsingSorting(arr,L,N):

    arr.sort()
    i = 0
    j = 1

    # Traverse the Array till last element.
    while i < L and j < L:

        # Base Condition
        if arr[j] - arr[i] == N:
            return True

        # if the Given Diff Number is greater than arr[j] - arr[i] that means we need to find bigger arr[j]  increase j by 1.
        elif (arr[j]-arr[i]) < N:
            j+=1

        # Else given diff is less than we have to maximize arr[i] , increase i by 1.
        else:
            i+=1
    return False


# Driver Method

arr = [5, 20, 3, 2, 5, 80]

if findPairGivenDiff(arr,len(arr),78):
    print(1)
else:
    print(-1)


