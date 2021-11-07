# Problem Statement : https://www.geeksforgeeks.org/cutting-a-rod-dp-13/
# Type : Unbounded Knapsack


# TC = O(L*N)
# SC = O(L*N)
def helperMethod(L,n,length,price,DP):

    if L == 0:return 0
    if n == 0:return 0

    if DP[n][L] != -1:
        return DP[n][L]
    if length[n-1] > L:
        DP[n][L] =  helperMethod(L,n-1,length,price,DP)
        return DP[n][L]

    include  = price[n-1]  + helperMethod(L-length[n-1],n,length,price,DP)     # N because we can use a single item many times.

    exclude = helperMethod(L,n-1,length,price,DP)

    DP[n][L]  = max(include,exclude)
    return DP[n][L]

def maximumPriceByCuttingRod(L,n,length,price):
    DP = [[-1 for _ in range(L+1)] for _ in range(n+1)]
    return helperMethod(L,n,length,price,DP)


# TC = O(L*N)
# SC = O(L*N)
def maximumPriceByCuttingRod_BottomUp(L,n,length,price):

    # Base case
    if L == 0 or n == 0:return 0

    DP = [[-1 for _ in range(L+1)] for _ in range(n+1)]
    for row in range(n+1):
        for col in range(L+1):
            if row == 0 or col == 0:
                DP[row][col] = 0

            else:
                # If current length is greater than rod Length then we can only exclude it.
                if length[row-1] > col:
                    DP[row][col] = DP[row-1][col]

                # Here we have two choices either to include current length or exclude.
                else:
                    exclude = DP[row-1][col]
                    include = price[row-1] + DP[row][col-length[row-1]]
                    DP[row][col]  = max(exclude,include)

    return DP[n][L]



# Driver Code
length = [1,2,3,4,5,6,7,8]
price = [1,5,8,9,10,17,17,20]
rodLength = 8
n = 8
print("Maximum value that can be obtained by cutting the rod is {}".format(maximumPriceByCuttingRod(rodLength,n,length,price,)))
print("Maximum value that can be obtained by cutting the rod is {}".format(maximumPriceByCuttingRod_BottomUp(rodLength,n,length,price)))
