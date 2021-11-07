# Problem Statement : https://www.geeksforgeeks.org/minimum-number-of-squares-whose-sum-equals-to-given-number-n/

# TC = Exponential as we are Using Simple Recursion.
def getMinSquares(n):
    # Base case
    if n <= 3:
        return n
    result = n
    i = 1
    while i*i <= n:
        result = min(result,1 + getMinSquares(n - i*i))
        i+=1

    return result

# DP Solution with Tabulation ( Bottom Up Approach ).
# TC = O(N * LogN)  SC = O(N)
def getMinSquares_DPTabulation(n):

    dp = [0,1,2,3]

    # Calculate all the answer before hand .
    for i in range(4,n+1):

        dp.append(i)

        j = 1
        # Loop through all the Possible perfect squares <= to the given i.
        while j*j <= i:
            dp[i] = min(dp[i],1+ dp[i - j*j])
            j+=1


    # At this step we will be having all the answer in the array .
    return dp[n]


# DP Solution with Memoization ( Top Down Approach )
def getMinSquares_DPMemoization(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = float("inf")
        j = 1

        while j*j <= i:
            dp[i] = min(dp[i],dp[i-j*j])
            j+=1

        dp[i] += 1 # As we will add 1 number to reach this step.

    return dp[n]



# Driver Code
N = 88
# print("Minimum Squares {}".format(getMinSquares(N)))
print("Minimum Squares {}".format(getMinSquares_DPTabulation(N)))
print("Minimum Squares {}".format(getMinSquares_DPMemoization(N)))

