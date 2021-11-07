# Problem Statement : https://www.geeksforgeeks.org/median-two-sorted-arrays-different-sizes-ologminn-m/?ref=rp
# Solution : https://www.youtube.com/watch?v=yD7wV8SyPrc


# TC = O(Log(Min(m,n))
# SC = O(1)
def getMedian(arr1,arr2):

    n1 = len(arr1)
    n2 = len(arr2)
    # If the length of the first array is greater than second array then return the second array as first parameter
    # This step is to ensure that complexity remain O(Log(Min(m,n))).
    if n1 > n2:
        return getMedian(arr2,arr1)

    low = 0
    high = n1

    while low <= high:

        # Get the Cut 1 & cut 2
        cut1 = (low + high) // 2

        cut2 = (n1+n2)//2 - cut1  # As we need equal elements in both sides that's why cut2 will be like that both half contains equal elements.

        # Not get the left elements of both the arrays if cut is not at the first element else assign inimum value.
        left1 = arr1[cut1-1] if cut1 else -float('inf')
        left2 = arr2[cut2-1] if cut2 else -float('inf')

        # Now get the right element of both the array .
        right1 = arr1[cut1] if cut1 < n1 else float('inf')
        right2 = arr2[cut2] if cut2 < n2 else float('inf')

        # Now check the Desired Condition if it's meeting the return the output.
        if left1 <= right2 and left2 <= right1:

            # If (n1+n2) %2 == 0 then
            if (n1 + n2) % 2 ==0:
                return (max(left1, left2) + min(right1, right2)) / 2

            # as there will be 1 extra element in the right sub array that's why return minimum of that.
            else:
                return min(right1,right2)


        elif left1 > right2:
            high = cut1 - 1

        else:
            low = cut1 + 1


    return 0.0





# Driver Code
arr1 = [2,3,4,5]
arr2 = [1]

print(getMedian(arr1,arr2))