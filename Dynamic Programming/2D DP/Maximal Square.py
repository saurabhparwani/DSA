# Problem Statement : https://leetcode.com/problems/maximal-square/
# TC = O(M*N)
# SC = O(M*N)
def maximalSquare(matrix):

    m = len(matrix)
    n = len(matrix[0])

    # Base case , if m or n is 0 then answer will be 0.
    if m == 0 or n== 0:return 0

    DP = [[0 for _ in range(n)] for _ in range(m)]
    maximum = 0

    for row in range(m):
        for col in range(n):

            # Base case
            if row == 0 or col == 0:
                DP[row][col] = int(matrix[row][col])

            elif matrix[row][col] == '1':
                DP[row][col] = 1 + min(DP[row-1][col-1],DP[row-1][col],DP[row][col-1])

            # Update the maximum each time.
            maximum = max(maximum,DP[row][col])

    return maximum*maximum




# Driver Code
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]


print("Area of maximum square formed by 1 is {}".format(maximalSquare(matrix)))