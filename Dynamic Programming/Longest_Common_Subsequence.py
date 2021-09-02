# Recursive Method to calculate the Maximum length of common sub sequence.
# If the last character of both the string are same then Calculate for strings excluding last characters.
# If the last character of both the string are not same then Calculate max length of (m-1,n) & (m,n-1) where m & n is the length of strings respectively.
# Worst Case TC =  O(2^n)
def longest_common_subsequence_recursion(X,Y,m,n):
    # Base Case
    if m == 0 or n == 0:
        return 0

    # Check for the condition where last characters from both the strings are same.
    elif X[m-1] == Y[n-1]:
        return  1 + longest_common_subsequence_recursion(X,Y,m-1,n-1)

    else:
        return max(
            longest_common_subsequence_recursion(X,Y,m,n-1),
            longest_common_subsequence_recursion(X,Y,m-1,n)
        )


# Calculate the maximum length of common sub sequence using DP.
# First row & first Column will be 0.
# Formula is DP[i][j] = DP[i-1][j-1] + 1 if X[m-1] == Y[n-1] else DP[i][j] = max(DP[i-1][j] , DP[i][j-1]).
def longest_common_subsequence_dp(X,Y,m,n):

    # Create the DP matrix consisting of None.
    DP = [[None] * (n+1) for i in range(m+1)]

    # Create the Conditions.
    for i in range(m+1):
        for j in range(n+1):
            # Make the first row & column as 0.
            if i == 0 or j == 0 :
                DP[i][j] = 0

            # If the last character matches in both the strings.
            elif X[i-1] == Y[j-1]:
                DP[i][j] = DP[i-1][j-1] + 1

            # DP[i][j] will be maximum of DP[i-1][j] and DP[i][j-1].
            else:
                DP[i][j] = max(DP[i-1][j],DP[i][j-1])

    # return the last cell of the matrix which will give the value of length of longest common sub sequence.
    return DP[m][n]

# Driver Code
X = "zxabcdezy"
Y = "yzabcdezx"
print("Length of LCS is {}".format(longest_common_subsequence_recursion(X , Y, len(X), len(Y))))
print("Length of LCS is {}".format(longest_common_subsequence_dp(X , Y, len(X), len(Y))))