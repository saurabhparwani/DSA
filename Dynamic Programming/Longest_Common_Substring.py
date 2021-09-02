# Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.
# Input : X = “GeeksforGeeks”, y = “GeeksQuiz”
# Output : 5
# Explanation:
# The longest common substring is “Geeks” and is of length 5.
#
# Input : X = “abcdxyz”, y = “xyzabcd”
# Output : 4
# Explanation:
# The longest common substring is “abcd” and is of length 4.
# Input : X = “zxabcdezy”, y = “yzabcdezx”
# Output : 6
# Explanation:
# The longest common substring is “abcdez” and is of length 6.

# Method to Calculate Longest Common Substring using recursion.
# This Method will Compare Last character of the both Strings and if it is same then check for the string length m-1 & n-1.
# If the last character of both the string is not the same then it will check for length m & n-1 and m-1 & n .
def LCSRecursive(m,n,count):
    # Base Case
    if m == 0 or n == 0:
        return count

    # If the Last Characters of both strings are same then Calculate for the length m-1 & n-1.
    if X[m-1] == Y[n-1]:
        count = LCSRecursive(m-1,n-1,count+1)

    # Find the Maximum Count
    count = max(count,max(LCSRecursive(m-1,n,0),LCSRecursive(m,n-1,0)))

    # Return Count
    return count


# Method to Calculate Longest Common Substring Using DP ( Bottom Up Fashion)
# TC = O(M * N)
# SC = O(M * N)
# Condition => DP[i][j] = DP[i-1][j-1] + 1 if X[m-1] == Y[n-1] & return the max value of DP Matrix.
def LCSUsingDP(X,Y,m,n):
    # Create the DP Table
    DP = [[ 0 for k in range(n+1)] for l in range(m+1)]

    # Declare the result variable to store the maximum length of substring.
    result = 0

    # Loop through the Complete Matrix and build the Matrix Acc to given Condition.
    for i in range(m+1):
        for j in range(n+1):
            # Mark the First row & column as 0.
            if i == 0 or j == 0:
                DP[i][j] = 0

            # If the Last character of the substring is same & calculate the maximum length of result.
            elif X[i-1] == Y[j-1]:
                DP[i][j] = DP[i-1][j-1] + 1
                result  = max(result,DP[i][j])

            # Else fill that cell as 0.
            else:
                DP[i][j] = 0

    # Return the result
    return  result

# Driver Code

X = 'zxabcdezy'
Y = 'yzabcdezx'

print("Maximum Length of Common Substring  {}".format(LCSRecursive(len(X),len(Y),0)))
print("Maximum Length of Common Substring  {}".format(LCSUsingDP(X,Y,len(X),len(Y))))

