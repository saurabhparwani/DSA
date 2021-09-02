def printSolution(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j] , end =" ")
        print()
    print("|||||||||||||||||||||||||||||||||||||||||")

# Method to check that is it safe to place queen at the current place or not .
# It will check in left Upper Diagonal & left bottom diagonal and in all columns of given row.
def isSafe(board,row,col):

    # Check that Queen is already placed in same row or not.
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check that Queen is already placed in Upper left diagonal or not.
    # If it is there then return false.
    i = row
    j = col
    while i >=0 and j >= 0:
        if board[i][j]=='Q':
            return False
        i-=1
        j-=1

    # Check that Queen is already placed in Bottom left diagonal or not.
    # If it is there then return false.

    i = row
    j = col
    while j >=0 and i<len(board):
        if board[i][j]=='Q' :
            return False
        j-=1
        i+=1

    return True


# Recusrive Function to Check that Whether we can Place a Queen at this column or not .
# If we can place the queen at the current place then check for next queen next column.

def solveNQueenUtility(board,col):

    N = len(board)

    #Base Case
    if col >= N:
        printSolution(board)
        return

    # Check that we can place a Queen in Particular row or not
    # If can place a queen in that row then place it and place next queen in next column by calling recursive function.
    for i in range(N):

        # Check for Safe Condition
        if isSafe(board,i,col):

            board[i][col] = 'Q'  # Mark Current Position in answer board

            # Now Check for Next Queen by Placing this in next column
            solveNQueenUtility(board,col+1)


            board[i][col] = '-'  # Backtrack if answer not Coming.

    # return result  # Return This if we can not place Queen in any row.


# Drive Function to Solve N Queen Problem
# This function will call recursive function and print the ChessBoard if there is some output.
def solveNQueen(n):

    board = [['-' for i in range(n)] for j in range (n) ]

    if n < 4:
        print("Solution Does Not Exist")
        return
    solveNQueenUtility(board,0)

N = int(input("Enter the Size of the ChessBoard : "))
solveNQueen(N)
