# Maze Size
N = 4
count = [0]


# Directions Array to store left,right,top,down direction
directions = [[1,0],[-1,0],[0,1],[0,-1]]

# A Utility Method to Print maze.
def printSolution(maze):
    for i in range(N):
        for j in range(N):
            print(maze[i][j],end = " ")
        print()
    print("------------------------------------")

# Method to check that current cell is
def isSafe(maze,x,y):
    # Check for boundary points and current cell is  active or dead.
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True

    return False

# A recursive Method to
def solveMazeUtil(maze,sol,x,y):

    # If x,y is goal then print solution matrix.
    if x == N-1 and y == N-1 and maze[x][y] == 1:
        sol[x][y] = 1
        count[0]+=1
        printSolution(sol)

    # Check for the Safe Condition
    if isSafe(maze,x,y):

        # Check if the current block is already part of solution path. if yes then return
        if sol[x][y] == 1:
            return

        sol[x][y] = 1

        # Check in all four direction
        for i,j in directions:
            solveMazeUtil(maze,sol,x+i,y+j)

        # Backtrack
        sol[x][y] = 0
        return

# Method to solve Maze problem .
def solveMaze(maze):
    sol = [[0 for i in range(N)] for j in range(N)]
    solveMazeUtil(maze,sol,0,0)
    if count[0] ==0:
        print("No Solution Exist")
    else:
        print("Total Ways " + str(count[0]))

# Driver program to test above function
if __name__ == "__main__":
    # Initialising the maze
    maze = [[1, 1, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 1]]

    solveMaze(maze)
