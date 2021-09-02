# Problem Statement :  https://www.geeksforgeeks.org/topological-sorting/
from collections import defaultdict

class Graph(object):

    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)


    def topologicalSortUtil(self,vertex,visited,stack):
        # Mark the current node as visited.
        visited[vertex] = True
        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[vertex]:
            if visited[neighbour] == False:
                self.topologicalSortUtil(neighbour,visited,stack)

        # Push current vertex to stack which stores result
        stack.append(vertex)

    def topologicalSort(self):
        visited = [False] * (self.V +1)
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)

        # Print the stack in reverse order
        print(stack[::-1])


# Driver Code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is a Topological Sort of the given graph")

# Function Call
g.topologicalSort()
