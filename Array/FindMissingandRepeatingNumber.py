# Problem Statement  : https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/

# Method 1 : Using Sorting , TC = O(N*LogN)  , SC = O(1)
# Method 2 : Using Hash map or count array. TC = O(N) , SC = O(N)
# Method 3 . Using Mathematical expression.  TC = O(N) , SC = O(1)
# Method 4 : Using XOR Operation . TC = O(N) , SC = O(1)



# Method 3 Using mathematical formula.
def findRepeatingMissingNumber(arr,n):

    # Calculate the actual sum * Square Sum by using mathematical formula
    actual_sum = (n*(n+1))//2
    square_sum = (n*(n+1)*(2*n+1)) // 6

    arr_sum = 0
    arr_sqa_sum = 0

    for i in range(0,n):
        arr_sum += arr[i]
        arr_sqa_sum += (arr[i]*arr[i])

    # Now as per the algorithm let Suppose X & Y are the missing and repeating number respectively.
    # Then actual_sum - arr_sum = X - Y & square_sum - arr_sqa_sum = X*X - Y*Y

    # X-Y
    sum1 = actual_sum - arr_sum

    # X+Y will be (square_sum - arr_sqa_sum ) // X-Y i.e actual_sum - arr_sum
    sum2 = (square_sum - arr_sqa_sum)//sum1

    y = (sum2 - sum1) // 2

    x = sum2 - y

    return [y,x]


# Driver code
arr =   [4, 3, 6, 2, 1, 1]

result = findRepeatingMissingNumber(arr,len(arr))

print("Repeating Number {}".format(result[0]))
print("Missing Number {}".format(result[1]))
