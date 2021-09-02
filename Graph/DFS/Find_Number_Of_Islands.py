# Problem Statement :  https://www.geeksforgeeks.org/find-number-of-islands/

class Graph(object):

    def __init__(self,row,col,g):
        self.row = row
        self.col = col
        self.graph = g

    def isSafe(self,x,y):

        if x > -1 and x < self.row and y > -1 and y < self.col and self.graph[x][y] == 1:
            return True

        return False

    def dfsUtility(self,x,y):

        if self.isSafe(x,y):

            # Mark Current coordinate as the visited island.
            self.graph[x][y]  = 2


            # Now Do DFS in all 8 possible directions.
            self.dfsUtility(x-1,y-1)
            self.dfsUtility(x,y-1)
            self.dfsUtility(x+1,y-1)
            self.dfsUtility(x+1,y)
            self.dfsUtility(x+1,y+1)
            self.dfsUtility(x,y+1)
            self.dfsUtility(x-1,y+1)
            self.dfsUtility(x-1,y)

    # TC = O(Row * Col) , In worst case each coordinate will be called  9 times , but overall it will be O(row * col)
    # SC = O(Row * Col ) , In worst case all the islands will be in the stack.
    def countIslands(self):
        count = 0
        for i in range(self.row):
            for j in range(self.col):
                # If the current coordinate is the unvisited Island then apply DFS.
                if self.graph[i][j] == 1:
                    self.dfsUtility(i,j)
                    count += 1

        return count


# Driver Code
graph = [[0,1,1,1,0,0,0],
         [0,0,1,1,0,1,0],]

row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)
total_islands = g.countIslands()
print("Total number of Islands {}".format(total_islands))