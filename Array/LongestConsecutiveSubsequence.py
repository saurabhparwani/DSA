from collections import Set
# Problem Statement : https://www.geeksforgeeks.org/longest-consecutive-subsequence/
# Method 1 . Naive Method using sorting technique.
# TC = O(N LOG N) SC = O(1)
def findLongestConseqSubseq(arr, n):
    ans = 0
    count = 0

    # Sort the array
    arr.sort()

    v = []

    v.append(arr[0])

    # Insert repeated elements only
    # once in the vector
    for i in range(1, n):
        if (arr[i] != arr[i - 1]):
            v.append(arr[i])

    # Find the maximum length
    # by traversing the array
    for i in range(len(v)):

        # Check if the current element is
        # equal to previous element +1
        if (i > 0 and v[i] == v[i - 1] + 1):
            count += 1

        # Reset the count
        else:
            count = 1

        # Update the maximum
        ans = max(ans, count)

    return ans


# Method 2 . Efficient Method using hashing.
# TC = O(N) SC = O(1)
def findLongestConseqSubseq(arr, n):
    s = set()
    ans = 0

    # Hash all the array elements
    for ele in arr:
        s.add(ele)

    # check each possible sequence from the start
    # then update optimal length
    for i in range(n):

        # if current element is the starting
        # element of a sequence
        if (arr[i] - 1) not in s:

            # Then check for next elements in the
            # sequence
            j = arr[i]
            while (j in s):
                j += 1

            # update  optimal length if this length
            # is more
            ans = max(ans, j - arr[i])
    return ans


# Driver code
if __name__ == '__main__':
    n = 7
    arr = [2,6,1,9,4,5,3]
    print ("Length of the Longest contiguous subsequence is {}".format(findLongestConseqSubseq(arr, n)))
