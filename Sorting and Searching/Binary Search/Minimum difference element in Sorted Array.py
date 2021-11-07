# Problem Statement : https://www.youtube.com/watch?v=3RhGdmoF_ac&list=PL_z_8CaSLPWeYfhtuKHj-9MpYb6XQJ_f2&index=15

# Approach : As the array is sorted so if the target is available in the array then minimum difference will be 0.
# If target is not in the array then find floor & ceil of target and return minimum absolute diff of ( target  - floor ) or ( Ceil - Target).

# As the array is sorted we can simply use binary search .
# TC = O(Log N)
# SC = O(1)
def findMinDiffTarget(arr,n,target):

    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:return 0
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # If we reach till this step then definitely low > high that means target is not in the array.
    # So now Low will be pointing to the ceil of the target & High will be pointing to the floor of the array.

    if low == n: # Special case when target is larger than the last element of the sorted array then low will be == n so to avoid index out of bound error.
        return (target - arr[low -1 ])

    if abs(arr[low]-target) > abs(target - arr[high]):
        return abs(target-arr[high])
    else:
        return abs(arr[low]-target)



# Driver Code
arr1 = [1,5,8,12,15,18]
target = 30

print("Minimum difference of target with given element is {}".format(findMinDiffTarget(arr1,len(arr1),target)))