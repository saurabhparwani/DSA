# Problem Statement : https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1
# Given a boolean 2D array of n x m dimensions where each row is sorted.
# Find the 0-based index of the first row that has the maximum number of 1's.

# Method 1 : We can traverse each row and count the Number of 1's in every row and in the end
# we will return rows with maximum 1. TC = O(M*N)
# Method 2 : As array is already sorted so we can apply binary search in the array to find
# the maximum 1's by using first & last occurance. TC = (N* logM)

# Method 3 : This is the efficient approach as we know that row is already sorted and only 0 & 1 are available
# so we will start from the top right and calculate the 1's and if we found the 0 then we will process from next rows.
# TC = O(M+N) as we are traversing matrix in stair manner. SC = O(1)
def find_Max_one(mat):
    N = len(mat)
    M = len(mat[0])
    maximum = -1

    # Check for proper matrix
    if N > 0 and M >0:
        j = M-1

        for i in range(0,N):
            # Traverse from right to left till we are getting 1.
            while j > -1 and mat[i][j] == 1:
                j -= 1
                maximum = i

        return maximum

# Driver Code
mat_1 = [[0, 1, 1, 1],[0, 0, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]]
mat_2 = [[0,0],[1,1]]

print(find_Max_one(mat_1))
print(find_Max_one(mat_2))
