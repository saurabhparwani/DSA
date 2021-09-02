# Problem Statement : https://www.geeksforgeeks.org/count-pairs-with-given-sum/
# Use the GFG method as it is more efficient.

# TC = O(N) SC = O(N)
def getPairsCount(self, arr, n, k):
    a = {}
    count = 0
    for ele in arr:

        if k - ele in a.keys():
            count += a[k - ele]

        if ele in a.keys():
            a[ele] += 1
        else:
            a[ele] = 1
    return count


# GFG Method more efficient as it is using hashing.
def getPairsCount(arr, n, sum):
    m = [0] * 1000

    # Store counts of all elements in map m
    for i in range(0, n):
        m[arr[i]] += 1

    twice_count = 0

    # Iterate through each element and increment
    # the count (Notice that every pair is
    # counted twice)
    for i in range(0, n):

        twice_count += m[sum - arr[i]]

        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is  decreased by one such
        # that the (arr[i], arr[i]) pair is not
        # considered
        if (sum - arr[i] == arr[i]):
            twice_count -= 1

    # return the half of twice_count
    return int(twice_count / 2)