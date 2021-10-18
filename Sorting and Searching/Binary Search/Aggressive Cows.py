# Problem Statement : https://www.youtube.com/watch?v=wSOfYesTBRk&list=PLgUwDviBIf0qYbL4TBaEWgb-ljVdhkM7R&index=9


# Utility Method to check that we can place given cows with given gap in the array of not.
def isPossible(arr,n,cows,gap):

    # Place the first cow to the first position and updated the count.
    placed_cows = 1
    lastPlacedCows = arr[0]

    # Now try to place all the cows.
    for i in range(1,n):
        if (arr[i] - lastPlacedCows >= gap):
            placed_cows += 1
            lastPlacedCows = arr[i]

    # Once the loop is completed check we able to place all the cows or not.
    if placed_cows == cows:
        return True
    else:
        return False

# TC = O(N* Log(high - low)) N for traversing the arr to put cows. Also we will max traverse whole array max Log(high-low) times.
# Casue we are first finding maximum gap which can be high - low and then we are doing Binary search in that array.

# SC = O(1)
def maximize_Minimum_Distance(arr,cows):

    # First Sort the Given array in case if it is not sorted.
    arr.sort()
    n = len(arr)
    low  = 1
    answer = 0
    high = arr[n-1] - arr[0]  # Maximum Gap between each cows can be last element - first element.

    # Now Do Binary Search and check Maximum Gap that we can have between each cows.
    while low <= high:

        mid = low + (high - low)//2

        # If we can place with given gap then move to the right side i.e find bigger gaps.
        if isPossible(arr,n,cows,mid):
            answer = mid
            low = mid + 1

        # Else reduce the gap i.e go to the left side.
        else:
            high = mid - 1

    return answer

# Driver Code

array = [1,2,4,8,9]
cows = 3
print("Maximum Distance is {}".format(maximize_Minimum_Distance(array,cows)))