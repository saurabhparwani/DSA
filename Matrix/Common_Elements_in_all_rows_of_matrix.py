# Problem Statement : https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/

# Method to print common elements of matrix  if element is present in all rows. Steps :
# 1. Store all the elements of first row in an map or dictionary which find keys in O(1) time.
# 2 . Now traverse the each row and check that element is present in map or not and also check for duplicate case
#     like if a element is occurring two times in a single row then count it's present only once and update map according to that.
# 3. In the end all the elements which exist in every row print all of them.
# TC = O(M*N)  , SC = O(N)   where M = Total rows , N = Total Columns

def printCommonElements(mat):

    # Check for proper matrix.
    if len(mat) > 0 and len(mat[0]) > 0:
        M = len(mat)
        N = len(mat[0])
        d = {}
        # Store all the unique elements of first row in a map/dictionary.
        for i in range(0,N):
            d[mat[0][i]] = 1

        # Now check for every element
        for i in range(1,M):
            for j in range(0,N):

                # Check that element is already present in map & check for duplicates as well like element should appear only once in a row.
                if mat[i][j] in d.keys() and d[mat[i][j]] == i :
                    d[mat[i][j]] += 1


                # Print if current row if is last row and element is present in all rows.
                    if i == M-1:
                        print(mat[i][j],end= " ")

# Driver Code
mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]

printCommonElements(mat)