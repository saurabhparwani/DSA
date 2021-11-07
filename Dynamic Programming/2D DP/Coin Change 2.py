# Problem Statement : https://leetcode.com/problems/coin-change-2/

# Top Down Memoization method .
# TC = O(N*Amount)
# SC = O(N*Amount)
def helper(coins,amount,n,DP):
    if amount == 0: return 1
    if n == 0: return 0

    # If the sub problem has been already solved then simply return pre calculated answer.
    if DP[n][amount] != -1:return DP[n][amount]

    if coins[n-1] > amount:
        DP[n][amount] = helper(coins,amount,n-1,DP)

    else:
        include =  helper(coins,amount-coins[n-1],n,DP)
        exclude = helper(coins,amount,n-1,DP)
        DP[n][amount] =  include + exclude     # Here we have to return total ways that's why we are returning this.

    return DP[n][amount]

def findTotalWays(coins,amount):
    n = len(coins)
    DP = [[-1 for _ in range(amount+1)]for _ in range(n+1)]
    return helper(coins,amount,n,DP)

# Bottom Up Approach of finding total ways to make coin combination. ( Top down is more optimized on Leet code question.
# TC = (N* Amount )
# SC = O(N*Amount)
def findTotalWays_BottomUp(coins,amount):

    if amount == 0:return 1
    n = len(coins)
    if n == 0:return 0

    DP = [[0 for _ in range(amount+1)] for _ in range(n+1)]

    for row in range(n+1):
        for col in range(amount+1):

            if col == 0:
                DP[row][col] = 1
            elif row == 0:
                DP[row][col] = 0

            else:
                if coins[row-1] > col:
                    DP[row][col] = DP[row-1][col]
                else:
                    include = DP[row][col - coins[row-1]]
                    exclude = DP[row-1][col]

                    DP[row][col] = include + exclude

    return DP[-1][-1]

# Bottom Up Space Optimized approach of finding total ways to make combination.
# TC = O(N*Amount)
# SC  = O(Amount)
def findTotalWays_SpaceOptimized(coins,amount):
    if amount == 0:return  1
    n = len(coins)
    if n == 0:return 0

    DP = [0 for _ in range(amount+1)]
    DP[0] = 1
    for coin in coins:
        for amt in range(coin,amount+1,1):
                DP[amt] +=  DP[amt - coin]   # Here + as we are looking for total ways.
    return DP[amount]

# Driver Problem
coins = [1,2,5]
amount = 5

print("Total number of ways to make given change {}".format(findTotalWays(coins,amount)))
print("Total number of ways to make given change {}".format(findTotalWays_BottomUp(coins,amount)))
print("Total number of ways to make given change {}".format(findTotalWays_SpaceOptimized(coins,amount)))
