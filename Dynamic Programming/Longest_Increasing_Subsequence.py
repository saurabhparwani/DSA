# Method to Calculate Longest Increasing Sub sequence using two loops.

# TC = O(N*N)
# SC = O(N)
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


# Driver Code
array = [5,8,3,7,9,1]
print("Maximum Length of Increasing Subsequence {}".format(LIS(array)))