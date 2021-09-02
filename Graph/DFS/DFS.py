from collections import defaultdict
# This class represents a directed graph
# using adjacency list representation
class Graph(object):

    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    # Function to add an Edge in graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def buildGraph(self):
        self.addEdge(0, 1)
        self.addEdge(0, 2)
        self.addEdge(1, 2)
        self.addEdge(2, 0)
        self.addEdge(2, 3)
        self.addEdge(3, 3)

    def dfsUtility(self,v,visited):
        visited.add(v)
        print(v,end=" ")
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfsUtility(neighbour,visited)

    def DFS(self):
        visited=set()
        for vertex in list(self.graph):
            if vertex not in visited:
                self.dfsUtility(vertex,visited)



g = Graph()
g.buildGraph()
g.DFS()


# Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
# Space Complexity :O(V).
# Since an extra visited array is needed of size V.