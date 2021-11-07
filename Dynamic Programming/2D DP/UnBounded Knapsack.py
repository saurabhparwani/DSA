# In 0-1 Knapsack a single element can be selected only once but in Unbounded knapsack a single element can be selected many times.

# Problem Statement : https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/

# TC = O(n*W)
# SC = O(n*W)
def helper(W,n,val,wt,DP):

    if W == 0:return 0        # Base Case 1
    if n == 0:return 0

    # Check that if the sub problem has been already solved or not.
    if DP[n][W] != -1:
        return DP[n][W]

    if wt[n-1] <= W:
        include = val[n-1] + helper(W-wt[n-1],n,val,wt,DP)   # n because we can duplicate items.
        exclude = helper(W,n-1,val,wt,DP)

        DP[n][W] =  max(include,exclude)        # Store the current result for future use .

    else: DP[n][W] =  helper(W,n-1,val,wt,DP)       # If the weight of the (n-1)th element is greater than knapsack limit.

    return DP[n][W]

def findmaximum_value_knapsack_TopDown(W,n,val,wt):
    DP = [[-1 for _ in range (W+1)] for _ in range(n+1)]  # DP table for memoization.
    return helper(W,n,val,wt,DP)

def findMaximumKnapsack_BottomUp(W,n,val,wt):

    if W == 0 or n == 0:
        return 0

    # Here n is representing the number of items in the list and W representing the current weight of the knapsack.
    DP  = [[-1 for _ in range(W+1)] for _ in range(n+1)]

    for row in range(n+1):
        for col in range(W+1):

            # Base case Handle
            if row == 0 or col == 0:
                DP[row][col] = 0
            else:
                # If current weight of the knapsack is greater than current knapsack capacity then we will exclude this item.
                if wt[row-1] > col:
                    DP[row][col] = DP[row-1][col]

                # If current weight of the knapsack is less than or equal to the knapsack capacity then we will take max of include & exclude case.
                else:
                    include = val[row-1] + DP[row][col - wt[row-1]]   # Here it will be row as we can  use a single element many times.

                    exclude = DP[row-1][col]
                    DP[row][col] = max(include,exclude)

    return DP[n][W]





# Driver Code
W = 100
val= [10, 30, 20]
wt = [5, 10, 15]
n = len(val)
print("Maximum value of the knapsack is {}".format(findmaximum_value_knapsack_TopDown(W,n,val,wt)))
print("Maximum value of the knapsack is {}".format(findMaximumKnapsack_BottomUp(W,n,val,wt)))