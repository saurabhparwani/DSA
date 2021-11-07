# Problem Statement : https://leetcode.com/problems/search-in-rotated-sorted-array/

# Helper method to find he index of the minimum element.
def getIndexofMinimumelemnt(arr,start,high,n):

    while start <= high:
        if arr[start] <= arr[high]:
            return start

        mid = (start+high) // 2

        nextt = (mid+1)%n
        prev= (mid - 1 + n) % n

        # Minimum elment condition.
        if arr[mid] <= arr[prev] and arr[mid] <= arr[nextt]:
            return mid

        elif arr[mid] <= arr[high]:
            high = mid - 1

        elif arr[mid] >= arr[start]:
            start = mid + 1

    return  -1


# Approach is the find the index of minimum element in the array let say ind because array is sorted so we need two sorted array to search.
# 1 array will be from start to ind-1 & ind to high.

# TC = O(LogN)
# SC = O(1)
def findIndexofElement(nums,n,target):

    low = 0
    high = n-1
    index = getIndexofMinimumelemnt(nums,0,n-1,n)
    if index != -1:

        # Check that in which sorted part target is Lying then search according to that .
        prev = (index - 1 +n) %n
        if nums[low] <= target <= nums[prev]:
            high = prev
        else:
            low = index

        while low <= high:

            mid = (low+high)//2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                high = mid - 1

            else:
                low = mid + 1

        return  - 1



# Driver Code
nums = [4,5,6,7,0,1,2]
target = 7
print("Index of the given target element is {}".format(findIndexofElement(nums,len(nums),target)))

