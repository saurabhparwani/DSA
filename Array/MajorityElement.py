# Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
# Output : 4
# Explanation: The frequency of 4 is 5 which is greater
# than the half of the size of the array size.
#
# Input : {3, 3, 4, 2, 4, 4, 2, 4}
# Output : No Majority Element
# Explanation: There is no element whose frequency is
# greater than the half of the size of the array size.

# Approach 1 Use two loops and count frequency of each element.
# Approach 2 .We will use Hashmap to store number as key and frequency of that number as value.

# Approach 3 We will use Moore's Voting Algorithm.
# This Algo has two step 1st one to find majority element & 2nd step is to verify that it is actually majority element.

# Method to find  majority element through Moore Voting Algo.
def findmajority(a):
    n = len(a)
    count = 0
    ele = -1

    # Traverse the Array
    for i in range(0,n):

        if count == 0:
            count += 1
            ele = a[i]

        elif a[i] == ele:
            count += 1

        else:
            count -= 1

    return ele


def isMajority(arr,ele):
    count = 0
    for i in arr:
        if i == ele:
            count+=1

    if count > len(arr)//2 : return True
    else: return False

arr = [3, 3, 4, 2, 4, 4, 2, 4]

# find the Majority Element
ele = findmajority(arr)

# Confirm that found element is actually
if isMajority(arr,ele):
    print(ele)
else:
    print("No Majority Element")