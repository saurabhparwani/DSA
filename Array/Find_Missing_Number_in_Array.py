# You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list.
# One of the integers is missing in the list. Write an efficient code to find the missing integer.
#
# Input: arr[] = {1, 2, 4, 6, 3, 7, 8}
# Output: 5
# Explanation: The missing number from 1 to 8 is 5
#
# Input: arr[] = {1, 2, 3, 5}
# Output: 4
# Explanation: The missing number from 1 to 5 is 4

# Approach 1 : Using the frequency array to store the occurance of the number starting from 1 to N and then find the element whose frequency is 0.

# Approach 2 : Using the Formula N(N+1) /2 ( Sum of numbers from 1 to N) . TC = O(N) SC = O(N).

# Approach 3 : Using the XOR Method. TC = O(N) , SC = O(1) ( Best Method as it avoid issue of over flow)

# Method to find the missing number in array by using 2nd approach.
# TC = O(N) , SC = O(1)
def findMissingNumber(arr):
    n = len(arr)  # So N will be n+1 as length of array is n-1 and numbers can be from 1 to n.
    N = n+1
    sum_of_arr = sum(arr)
    missing_number = (N*(N+1))//2 - sum_of_arr
    print("Missing Number is {}".format(missing_number))


# Method to find the Missing number from an array using XOR method.( 3rd Approach )
# TC = O(N) , SC = O(1).
def findMissingUsing_XOR(arr):

    a = b = 0
    n = len(arr)
    for i in range(1,n+2):
        a = a^i

    for i in arr:
        b = b^ i

    print("Missing number is {}".format(a^b))

# Driver Code
arr = [1, 2, 4, 5, 6]
findMissingNumber(arr)
findMissingUsing_XOR(arr)


# Follow Up Question : Given and array and two numbers are missing so find the both numbers.
# Method to find the two missing number from array.
def findTwoMissingNumber(arr):
    # Total Number of elements
    N = len(arr) + 2
    ideal_sum =  (N*(N+1))//2
    actual_sum = sum(arr)
    avg = (ideal_sum-actual_sum)//2
    left_avg = right_avg = 0

    # Calculate the left & right Sum before & after avg element
    for i in arr:
        if i <=avg: left_avg+=i
        else:right_avg+=i

    # Now First Missing element will be (Total ideal sum from 1 to avg - actual sum till avg in given array)
    print("First Missing Number is {}".format(((avg*(avg+1))//2)-left_avg))

    # Now Second missing number will be (Total ideal sum from avg+1 number to N - actual sum of right half after avg)
    print("Second Missing Number is {}".format(((N*(N+1)))//2 - ((avg*(avg+1))//2)- right_avg))

# Method to find the
arr1 = [1, 3, 5, 6]
findTwoMissingNumber(arr1)

arr2 = [1, 2, 4]
findTwoMissingNumber(arr2)

arr3 = [1, 2]
findTwoMissingNumber(arr3)