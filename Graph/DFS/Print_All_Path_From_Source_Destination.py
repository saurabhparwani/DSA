# Problem Statement : https://www.geeksforgeeks.org/find-paths-given-source-destination/
from collections import defaultdict

class Graph(object):

    def __init__(self,V):
        self.vertices = V
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)


    def dfs(self,source,dest,visited,path):

        # Mark the current node as visited and store in path
        visited[source] = True
        path.append(source)

        # If current vertex is same as destination, then print current path[]
        if source == dest:
            print(path)

        else:

            # If current vertex is not destination Recur for all the vertices adjacent to this vertex
            for neighbours in self.graph[source]:
               if visited[neighbours] == False:
                  self.dfs(neighbours,dest,visited,path)

        # Remove current vertex from path[] and mark it as unvisited
        visited[source] = False
        path.pop()


    # TC = O(E+V) We are simply doing DFS Traversal.
    # SC = O(V) Bcoz at max all vertex will be in the path and O(V) for recursion space.
    def printAllPaths(self,source,dest):
        # Create an array to store paths
        visited = [False] * (self.vertices)
        path = []

        # Call the recursive helper function to print all paths
        self.dfs(source,dest,visited,path)




# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)

source = 2
dest = 3

print("Paths from source to destination are :")
g.printAllPaths(source,dest)

