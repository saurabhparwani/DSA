# Problem Statement :  https://www.geeksforgeeks.org/minimum-steps-reach-target-knight/

class cell(object):
    def __init__(self,x=0,y=0,dist=0):
        self.x = x
        self.y = y
        self.dist = dist

def isInside(x,y,N):
    return x >= 1 and x <= N and y >= 1 and y <= N

# TC  = O(N*N)  At worst case, all the cells will be visited so time complexity is O(N^2).
# SC = O(N*N)  The nodes are stored in queue. So the space Complexity is O(N^2).
def minStepToReachTarget(knightPos,targetPos,N):

    # all possible movments for the knight
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = []

    # push starting position of knight with 0 distance
    queue.append(cell(knightPos[0],knightPos[1],0))

    # make all cell unvisited
    visited = [[False for i in range(N + 1)] for j in range(N + 1)]

    # visit starting state
    visited[knightPos[0]][knightPos[1]] = True

    while queue:    # loop until we have one element in queue

        t = queue.pop(0)

        # if current cell is equal to target cell, return its distance
        if (t.x == targetPos[0] and t.y == targetPos[1]):
            return t.dist

        for i in range(8):    # iterate for all reachable states
            x = t.x + dx[i]
            y = t.y + dy[i]

            # If cell is inside Board and not visited already.
            if  isInside(x,y,N) and not visited[x][y]:
                visited[x][y] = True
                queue.append(cell(x,y,t.dist+1))


# Driver Code
N = 30
knightPos = [1,1]
targetPos = [30,30]

print(minStepToReachTarget(knightPos,targetPos,N))