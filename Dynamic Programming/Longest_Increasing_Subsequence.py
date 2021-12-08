# Method to Calculate Longest Increasing Sub sequence using two loops.
from collections import defaultdict

# TC = O(N*N)
# SC = O(N)
# Follow Up method to extend this method to print the LIS.
def LIS(arr):
   maxi = 1
   n = len(arr)
   LIS = [1] * n

   for i in range(1,n):
       for j in range(0,i):
           # Put the Condition
           if arr[i] > arr[j] and LIS[i] < LIS[j]+1:
               LIS[i] = LIS[j] + 1
               maxi = max(maxi, LIS[i])

   return maxi


def printLIS(arr):
    mapper = defaultdict(list)
    n =   len(arr)
    LIS = [1]*n

    mapper[arr[0]] =  [arr[0]]
    temp_max = 1
    max_key = 1
    max_lis = 1
    for i in range(1,n):
        mapper[arr[i]] = [arr[i]]       # Create list with single item.
        temp_max = -1
        for j in range(0,i):
            if arr[i] > arr[j] and LIS[j] + 1 > LIS[i]:
                LIS[i]= LIS[j] + 1
                # Store the key of the maximum element.
                temp_max = arr[j]

                # Get the key of teh maximum list.
                if max_lis < LIS[i]:
                    max_lis = LIS[i]
                    max_key = arr[i]

        if temp_max!= -1:
             mapper[arr[i]] = mapper[temp_max] + [arr[i]]     # update the new list.

    print(mapper[max_key])




# Driver Code
array = [3, 2, 6, 4, 5, 1]
print("Maximum Length of Increasing Subsequence {}".format(LIS(array)))
printLIS(array)