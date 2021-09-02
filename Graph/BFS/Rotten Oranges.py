# Problem  : https://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/
from collections import deque
# Method 1 : Brute Force
# Approach: The idea is very basic. Traverse through all oranges in multiple rounds.
# In every round, rot the oranges to the adjacent position of oranges which were rotten in the last round.


# Method 2 : Optimized Approach Using BFS.

# Time Complexity: O( R *C).
# Each element of the matrix can be inserted into the queue only once so the upper bound of iteration is O(R*C), i.e. the number of elements. So time complexity is O(R *C).
# Space Complexity: O(R*C).  To store the elements in a queue O(R*C) space is needed.

def minimumTimeRottenOranges(grid):

    # Base Case
    if grid is None or len(grid) == 0:
        return 0

    rows = len(grid)
    col = len(grid[0])
    # Initialize a Queue
    queue = deque()

    # To count the number of 2 & 1 in grid.
    count_fresh = 0

    # Append every rotten orange 2 in queue and count the fresh & rotten oranges n grid.
    for i in range(rows):
        for j in range(col):
            # Enqueue rotten orange
            if grid[i][j]== 2:
                queue.append([i,j])

            if grid[i][j] != 0:
                count_fresh +=1

    # If Matrix if of fully 0.
    if count_fresh == 0:
        return 0

    countMinTime = 0
    cnt = 0

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    # Pop points from queue till queue is not empty.
    while queue:

        # Collect the total element present in queue at a particular time.
        size = len(queue)
        cnt += size

        # Pop all the elements from queue.
        for i in range(size):
            point = queue.popleft()

            # Traverse in all 4 directions.
            for j in range(4):
                x = point[0]+dx[j]
                y = point[1]+dy[j]

                # Boundary & other checks
                if x < 0 or x >= rows or y < 0 or y >= col or grid[x][y] == 2 or grid[x][y]==0:
                    continue

                # If grid is 1 or fresh orange then rot it and append this in queue.
                grid[x][y] = 2
                queue.append([x,y])

        # If queue is not empty means that iteration added some new rotten orange in queue so increase the time count.
        if len(queue) != 0:
            countMinTime+=1

    # If total count is total number of 1 & 2 in grid then return minTime else it is impossible to rot all the oranges.
    if count_fresh == cnt:
        return countMinTime
    else: return -1

# Driver Code
arr = [[2, 1, 0, 2, 1],
       [1, 0, 1, 2, 1],
       [1, 0, 0, 2, 1]
      ]

print("Minimum time to Rot all oranges is {}".format(minimumTimeRottenOranges(arr)))