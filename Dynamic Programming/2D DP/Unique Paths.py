# Problem Statement :

# TC = O(M*N)
# SC = O(M*N)
def getTotalWays(m,n):
    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(0, n): dp[0][i] = 1
    for j in range(0, m): dp[j][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


def helper(x,y,m,n,dp):
    if x < 0 or x >= m or y<0 or y>=n:return 0
    if x == m-1 and y == n-1:return 1

    # Check if the sub problem is already solved or not.
    if (x,y) in dp:
        return dp[(x,y)]

    # Move in the down & right direction and get the count of the solution.
    count =  helper(x+1,y,m,n,dp) + helper(x,y+1,m,n,dp)

    dp[(x,y)] = count      # Memoize the count variable to store existing sub problem.
    return count

def getTotalPaths(m,n):
    dp = {}   # To Store the SubProblem Results
    return helper(0,0,m,n,dp)

m = 50
n = 50

print("Total Unique paths are {} ".format(getTotalPaths(m,n)))