# Simple Function to Print Matrix

def printMatrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end = " ")
        print()
    print("-----------------------------------")

# Method to create & return transpose Matrix of given square Matrix  ( Takes Extra Space )
def transpose_of_square_Matrix(matrix):
    n = len(matrix)
    b = [[ 0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            b[i][j]= matrix[j][i]
    printMatrix(b)


# Method to change Square Matrix to it's Transpose Matrix  ( In Place Algo no need to use extra matrix )

def transpose_of_square_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    printMatrix(matrix)


# Method to rotate a Matrix / Image 90 degree Clockwise without using extra space

def rotateMatrixClockwise(matrix):

    # Convert the matrix to it's transpose
    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    # To Rotate the Matrix 90 degree clockwise simply  reverse every row.

    for i in range(n):
        for j in range(0,n//2):
            matrix[i][j],matrix[i][n-1-j] = matrix[i][n-1-j],matrix[i][j]

    printMatrix(matrix)


def rotateMatrixAntiClockwise(matrix):
    # Convert the matrix to it's transpose
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # To Rotate the Matrix 90 degree clockwise simply  reverse every Column

    for i in range(n):
        for j in range(0, n // 2):
            matrix[j][i],matrix[n-1-j][i] = matrix[n-1-j][i],matrix[j][i]

    printMatrix(matrix)


a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
b = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
printMatrix(a)
rotateMatrixClockwise(a)
rotateMatrixAntiClockwise(b)

