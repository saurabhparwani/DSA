# Program to Print the Solution of Sudoku Puzzle

global N
N = 9
# Utility Method to test that is it safe to put a particular number in a cell such that  number should not exist in same row , col & 3*3 Matrix.
def isSafe(grid,row,col,num):

    # Check that if the number exist in the same row or not.
     for i in range(0,N):
         if grid[row][i] == num:
             return False

    # Check if the number exist in the same column or not.
     for i in range(0,N):
        if grid[i][col] == num:
            return False

     # Check that number already exist in 3 * 3 Matrix.
     pt_row = row//3 *3
     pt_col = col//3*3
     for i in range(3):
         for j in range(3):
             if grid[pt_row+i][pt_col+j] == num:
                 return False

     # If any of the condition is not true then return false.
     return True

# Method to Solve the Sudoku . This method will use recursion & backtracking technique to solve the sudoku.
# It will try tp place each number from 1-9 in a cell and then if that mive is safe then it will
def solveSudoku(grid,row,col):

    # Base Case when we reach to the last row & last column. Which means all the selections were correct and hence sudoku is solved.
    if row == N-1 and col == N:
        return True

    # If we reached at the end of the row then start from first column of the next row
    if col == N:
        row = row + 1
        col = 0

    # If the cell value is non zero then solve for the next cell for that row as we can not modify the existing values.
    if grid[row][col] > 0 :
        return solveSudoku(grid,row,col+1)

    # Else start from number 1 to 9 and then check which number is safe to place in that particular cell
    # If it is not safe the backtrack the change and repeat same process for other number.

    for i in range(1,N+1):

        # Number is safe to place
        if isSafe(grid,row,col,i):

            # Place the Number to that cell
            grid[row][col] = i

            # Solve for the next cell
            if solveSudoku(grid,row,col+1):
                return True

            # BackTrack if the previous selection was wrong
            grid[row][col] = 0

    # If any of the combinaton is not working then return false
    return  False


# Utility Method to Print the Sudoku.
def printSolution(grid):
    N = len(grid)
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end =" ")
        print()

# 0 means unassigned cells
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]


# Driver Method to test the code.
if solveSudoku(grid,0,0):
    printSolution(grid)
else:
    print("No Solution exist for this Sudoku")
