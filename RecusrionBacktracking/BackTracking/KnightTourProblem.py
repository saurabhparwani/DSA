def printChessBoard(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()

# Method to check that whether the move by Knight is Valid move or not
def isValid(x,y,n,board):

    # To check that Position lies in Chess Board and location is empty or not
    if x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1 :
        return True

    return False


def knightCanCoverCompleteChessBoard(board,pos,row_moves,col_moves,x,y,n):
    if pos == n**2:
        return True
    for i in range(8):
            row_position = x + row_moves[i]
            col_position = y + col_moves[i]
            if isValid(row_position,col_position,n,board):
                # Mark Current Position as possible Solution
                board[row_position][col_position] = pos

                # Call Recursive Method Again
                if (knightCanCoverCompleteChessBoard(board,pos+1,row_moves,col_moves,row_position,col_position,n)):
                    return True

                # Backtrack
                board[row_position][col_position] = -1
    return  False




# Method to Solve the Knight Tour Problem. This Method will make initially move and work as a driver method.
# This will Call recursive method and if solution exist then it will print that solution.
def solveKnightTourProblem(n):

    # Store all 8 moves which knight can take
    # This Combination of Array Will give Optimized solution as in this order Knight is moving circularly.
    row_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    col_moves = [1, 2, 2, 1, -1, -2, -2, -1]

    board = [[-1 for i in range(n)] for j in range(n)]

    # Initialize the starting Position and put knight at (0,0)  position
    pos = 1
    board[0][0] = 0

    if knightCanCoverCompleteChessBoard(board,pos,row_moves,col_moves,0,0,n):
        printChessBoard(board,n)
    else:
        # print("Knight Can not cover Complete ChessBoard")
        printChessBoard(board,n)
# Size of the ChessBoard
N = 8
solveKnightTourProblem(N)


















