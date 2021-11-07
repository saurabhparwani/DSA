# Problem Statement : https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
# Video Solution : https://www.youtube.com/watch?v=mGfK-j9gAQA

# TC of this Normal Recursive solution is (2^n) as we have two choices for each item.
# SC = O(1) Ignoring the stack space.

# Method 2 : Using Memoization DP
# TC = O(W*N)
# SC = O(W*N) + Stack Space for Recursion
def knapSack(W,val,wt,n,DP):

    # Base Case
    if W == 0 or n == 0:return 0

    # Check that if the sub problem has been already solved or not.

    # If weight of the (n-1)th item is the W , value of knapsack then we can't include this item in our knapsack.
    # So we will ignore that item and process for next element.
    if wt[n-1] > W:

        # For memoization instead of returning this Store the result first & then return.
        DP[n][W] = knapSack(W,val,wt,n-1,DP)
        return DP[n][W]

    # Else here we have two choices either include the current item or don't include that.
    # We will do in both ways and find maximum of that and will return  that.
    include = val[n-1] + knapSack(W-wt[n-1],val,wt,n-1,DP)

    exclude = knapSack(W,val,wt,n-1,DP)

    DP[n][W] =  max(include,exclude)

    return DP[n][W]
def getMaximumKnapsack_TopDown(W,val,wt,n):
    DP = [[-1 for col in range(W+1)] for row in range(n+1)]
    return knapSack(W,val,wt,n,DP)


# Method 3 : Using tabulation DP Bottom Up manner.
# TC = O(N*W)
# SC = O(N*W) : No extra space for stack space
def getMaximumKnapsack_BottomUp(W,val,wt,n):

    # Base case:
    if W == 0 or n== 0:return 0

    DP =  [[0 for col in range(W+1)] for row in range(n+1)]

    # We are starting from 1 as for row or col == 0 is the base case and answer will be 0 in that case.
    for row in range(1,n+1):
        for col in range(1,W+1):

            # Case 1 if the weight of the current item is greater than knapsack capacity , in that case we were not picking that element.
            # So the iterative form of this is.

            # Here Col represent the current weight capacity. And wt[row-1] is showing weight of the current item as we are representing item as row.
            # In that case do noting and go to next element.
            if wt[row-1] > col:
                DP[row][col] = DP[row-1][col]

            else:
                exclude = DP[row-1][col]

                # In include case we are calculating value of current item + then maximum value with updated n & W/
                include = val[row-1] + DP[row-1][col-wt[row-1]]

                DP[row][col] = max(include,exclude)

    # This represent the final answer maximum weight after n item & W knapsack capacity.
    return DP[n][W]




# Driver Code
val = [1,2,3]
wt = [4,5,6]
W = 4
n = len(wt)

print("Maximum Value that can be obtained from the knapsack is {}".format(getMaximumKnapsack_TopDown(W,val,wt,n)))
print("Maximum Value that can be obtained from the knapsack is {}".format(getMaximumKnapsack_BottomUp(W,val,wt,n)))