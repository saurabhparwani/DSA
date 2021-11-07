# Problem Statement : https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/


# TC = O(Log(Min(n,m))
# SC = O(1) 
def KthElement(arr1,arr2,n,m,k):

    # If n > m then swap the input because we want to apply binary search on the smaller array to maintain TC O(Log(Min(n,m))
    if n > m:
        return KthElement(arr2,arr1,m,n,k)

    # Initialize low and high

    # Because minimum selected element can be max of 0 or  k-m in case we have selected all the elements from
    # the  another array and still k > 0. So we have to select element from the second array.
    low = max(0,k-m)

    # Max number of element we can select from smaller array is minimum of k or n( all elements )
    high = min(k,n)

    while low <= high:

        cut1 = (low+high) // 2
        cut2 = k - cut1   # As we want k elements in the left side for our question.

        left1 = arr1[cut1-1] if cut1 else -float("inf")
        left2 = arr2[cut2-1] if cut2 else -float("inf")

        right1 = arr1[cut1] if cut1 < n else float("inf")
        right2 = arr2[cut2] if cut2 < m else float("inf")

        # Now check the Condition
        if left1 <= right2 and left2 <= right1:
            # Maximum of left side will be Kth element as there are only K element in the left side so we can only compare left1 & left2.
            return max(left1,left2)

        elif left1 > right2:
            high = cut1 - 1

        else:
            low = cut1 + 1

    return 1


# Driver Code

arr1 = [2, 3, 6 ,7 ,9]
arr2 = [1,4, 8 ,10]

k = 5

print("Kth element of the sorted array is {}".format(KthElement(arr1,arr2,len(arr1),len(arr2),k)))