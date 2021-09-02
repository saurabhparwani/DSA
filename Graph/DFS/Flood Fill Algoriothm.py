# Problem Statement : https://leetcode.com/problems/flood-fill/
import  queue

def isSafe(grid,x,y,n,m,oldColor):
    if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != oldColor:
        return False
    return True
def dfs(grid,x,y,n,m,oldColor,newColor):

    if not isSafe(grid,x,y,n,m,oldColor):
        return

    # Apply new Color to the found coordinate.
    grid[x][y] = newColor
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]

    # Now Traverse in the all four directions.
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]

        # Call DFS method recursively.
        dfs(grid,cx,cy,n,m,oldColor,newColor)

# TC = O(N*M)
# SC = O(N*M) For recursion stack.
def floodFill(grid,x,y,newColor):
    if grid:
        n = len(grid)
        m = len(grid[0])
        oldColor = grid[x][y]
        dfs(grid,x,y,n,m,oldColor,newColor)
    return grid


# Solution Using BFS.
# TC = O(N*M)
# SC = O(N*M) For Updated set & Queue in Worst Case.
def floodFillUsingBFS(grid,x,y):

    if grid:

        n = len(grid)
        m = len(grid[0])

        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        que = queue.Queue()

        oldColor = grid[x][y]
        updated =set()
        # Append the given coordinate into the Queue.
        que.put([x,y])

        # Traverse till queue is not empty.
        while que:

            # Fetch the row & Col or the  coordinate
            [row,col] = que.get()
            # Add into the updated set to avoid duplicate calls and change it;s color to newColor.
            updated.add((row,col))
            grid[row][col] = newColor

            # Find in all 4 directions.
            for dir in directions:
                dx = row + dir[0]
                dy = col + dir[1]
                # If coordinate is Valid. Add that into queue and repeat the above Process.
                if isSafe(grid,dx,dy,n,m,oldColor) and (dx,dy) not in updated:
                    que.put([dx,dy])

        # Finally return the updated image.
        return grid

# Driver Code

grid = [[0,0,0],[0,0,0]]

x = 0
y = 0
newColor = 2

# grid = floodFill(grid,x,y,newColor)

grid = floodFill(grid,x,y,newColor)
print(grid)

