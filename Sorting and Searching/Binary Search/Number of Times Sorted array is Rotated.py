# Problem Statement : https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/


# TC = O(LogN)
# SC = O(1)
def arrayRotatedCount(arr,n):

    low = 0
    high = n - 1

    # While looking at the problem we can say that number of times array is sorted is equal to the index of minimum element.
    # Minimum element will be lesser than it's next & previous element.
    while low <= high:

        # if the search space is already sorted then minimum element will be in start.
        if arr[low] <= arr[high]:
            return low

        mid = (low+high) // 2

        # Find the next & prev index of mid index % by n to handle corner indexes.
        next = (mid+1) % n
        prev = (mid-1+n) % n

        # Check that whether mid is the minimum element or not.If it is then return this index.
        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return mid

        # if nums[left…mid] is sorted, then the pivot element cannot be present in it;
        # discard nums[left…mid] and search in the right half
        elif arr[mid] >= arr[low]:
            low = mid + 1

        # if nums[mid…right] is sorted, and `mid` is not the minimum element, then the pivot element cannot be present in nums[mid…right],
        # discard nums[mid…right] and search in the left half
        elif arr[mid] <= arr[high]:
            high = mid - 1

    # Return -1 in case of invalid output.
    return -1



# Driver Code
arr = [1, 2, 3, 4, 5, 6, 7,8, 9, 10 ]
print("Number of time sorted array is rotated {}".format(arrayRotatedCount(arr,len(arr))))