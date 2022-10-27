# Problem : https://leetcode.com/problems/coin-change/

# Top Down ( Memoization method to get minimum number of coins required to make the required coin change)
# TC = O(Amount * N)
# SC = O(N*Amount)  where N is the length of the coins list.
def helperMethod(coins,amount,n,DP):

    # Base Case 1:
    if amount == 0: return 0

    # Base Case 2
    if n < 0:return float("inf")

    # If the sub problem has been already solved then simply return the previously calculated answer.
    if DP[n][amount] != -1:
        return DP[n][amount]

    # If current coin is the greater than amount than ignore that amount.
    if coins[n-1] > amount:
        DP[n][amount]  = helperMethod(coins,amount,n-1,DP)
        return DP[n][amount]

    # Else we can have two choices either to include or exclude the coin.
    include = 1 + helperMethod(coins,amount - coins[n-1],n,DP)      # +1 as we are counting the coins.
    exclude = helperMethod(coins,amount,n-1,DP)
    DP[n][amount] = min(include,exclude)
    return DP[n][amount]

def minimumCoins(coins,amount):
    n = len(coins)
    DP = [[-1 for _ in range(amount+1)] for _ in range(n+1)]
    ans =  helperMethod(coins,amount,n,DP)
    return -1 if ans == float("inf") else ans

# Bottom Up Approach of calculating minimum number of coins.
# TC = O(N*Amount)
# SC = O(N*Amount)
def minimumCoins_BottomUp(coins,amount):

    if amount == 0:return 0 # Base case 1

    n = len(coins)
    if n == 0:return -1   # base case 2

    DP = [[float("inf") for _ in range(amount+1)] for _ in range(n+1)]

    for row in range(n+1): # As first row means amount is 0 in coins list is empty in this case return -1.
        for col in range(amount+1):
            # handle base case if amount is 0 then:

            if col == 0:
                DP[row][col] = 0

            elif row == 0:
                DP[row][col] = float("inf")

            else:
                # If current coin is bigger than amount then exclude it and go to next coin.
                if coins[row-1] > col:
                    DP[row][col] = DP[row-1][col]
                else:
                    # Else include & exclude it and based upon the minimum value select this.
                    exclude = DP[row-1][col]
                    include = 1 + DP[row][col - coins[row-1]]
                    DP[row][col] = min(include,exclude)

    return -1 if DP[-1][-1] == float("inf") else DP[-1][-1]

# Space Optimized method for finding minimum number of coins.
# TC = O(N*Amount)
# SC = O(Amount)
def findMinimumCoins_BottomUp_Optimized(coins,amount):
    if amount == 0:return 0
    n = len(coins)
    if n==0:return -1

    DP = [float("inf") for _ in range(amount+1)]
    DP[0] = 0

    for amt in range(1,amount+1):
        for i in range(n):
            if coins[i] <= amt:
                DP[amt] = min(DP[amt],1+ DP[amt - coins[i]])

    return -1 if DP[amount] == float("inf") else DP[amount]




# Driver Code
coins = [2]
amount  = 13

print("Minimum number of coins to make the required amount {}".format(minimumCoins(coins,amount)))
print("Minimum number of coins to make the required amount {}".format(minimumCoins_BottomUp(coins,amount)))
print("Minimum number of coins to make the required amount {}".format(findMinimumCoins_BottomUp_Optimized(coins,amount)))
