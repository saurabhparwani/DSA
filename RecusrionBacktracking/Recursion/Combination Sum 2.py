# Problem Statement : https://leetcode.com/problems/combination-sum-ii/
# Video Solution : Take U Forward Recursion Playlist.


def findCombinations(arr,index,target,ds,answer):

    # Base Case if target is 0 then add this combination into the answer list.
    if target == 0:
        answer.append(list(ds))
        return

    for i in range(index,len(arr)):

        if i > index and arr[i] == arr[i-1]:     # To avoid the duplicate Combination
            continue

        if arr[i] > target:    # If element is greater than target then simply break the loop.
            break

        ds.append(arr[i])
        findCombinations(arr,i+1,target-arr[i],ds,answer)   # Call the same recursive method for the next index .
        ds.pop()   # Backtrack to remove the added element


# Wrapper method to call recursive method.
# TC = O(2^n)*K : ( As there will be total 2^n sub sequence of the given list & assuming that K will be length of the sub sequence)
# SC = O(k*x) (Assuming that there will be total x combination total of length k each.)

def combinationSum2(arr,target):
    answer = []
    ds = []
    arr.sort()   # Sort the array to find all the elements in lexicographically increasing order.
    findCombinations(arr,0,target,ds,answer)
    return answer


# Driver Code

arr = [10,1,2,7,6,1,5]
target = 8
ans = combinationSum2(arr,target)
print(ans)