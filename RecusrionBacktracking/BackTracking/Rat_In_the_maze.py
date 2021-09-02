# Maze Size
N = 4

# Directions Array to store left,right,top,down direction
directions = [[1,0],[-1,0],[0,1],[0,-1]]

# A Utility Method to Print maze.
def printSolution(maze):
    for i in range(N):
        for j in range(N):
            print(maze[i][j],end = " ")
        print()

# Method to check that current cell is
def isSafe(maze,x,y):
    # Check for boundary points and current cell is  active or dead.
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True

    return False

# A recursive Method to
def solveMazeUtil(maze,sol,x,y):

    # If x,y is goal then return true.
    if x == N-1 and y == N-1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    # Check for the Safe Condition
    if isSafe(maze,x,y):

        # Check if the current block is already part of solution path.
        if sol[x][y] == 1:
            return False

        sol[x][y] = 1

        # Check in all four direction
        for i,j in directions:
            if solveMazeUtil(maze,sol,x+i,y+j):
                return True

        sol[x][y] = 0
        return False

# Method to solve Maze problem .
def solveMaze(maze):
    sol = [[0 for i in range(N)] for j in range(N)]

    if solveMazeUtil(maze,sol,0,0) == False:
        print("No Solution exist")
        return

    printSolution(sol)


# Driver program to test above function
if __name__ == "__main__":
    # Initialising the maze
    maze = [[1, 1, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 1]]

    solveMaze(maze)