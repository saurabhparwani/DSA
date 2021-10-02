# Problem Statement : https://leetcode.com/problems/number-of-operations-to-make-network-connected/
from collections import defaultdict
class Graph(object):
    def __init__(self,V):
        self.V = V
        self.graph = defaultdict(list)
        self.edges = 0

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def makeGraph(self,edges):
        for edge in edges:
            self.addEdge(edge[0],edge[1])
            self.edges = self.edges + 1

    def dfs(self,node,visited):
        visited[node] = True
        for nbh in self.graph[node]:
            if visited[nbh] == False:
                self.dfs(nbh,visited)

    # TC = O(V+E) As we are doing simple DFS of a graph.
    # SC = O(V+V) For visited array and recursion depth.
    def minimumWireToMakeConnections(self):

        total_components = 0
        total_edges = self.edges
        n = self.V
        visited = [False]*(n+1)

        # Find the total number of components in the Graph.
        for node in range(n):
            if visited[node] == False:
                total_components = total_components + 1
                self.dfs(node,visited)

        # Base Case if total edges are less than n-1 then simply return -1.

        if total_edges < n-1:
            return -1

        # Find the total number of extra edges in the graph including all the components by formula.
        redun_edges = total_edges - ((n-1) - (total_components-1))

        if redun_edges < total_components - 1:
            return -1
        else:
            return total_components - 1

# Driver Code
n = 5
connections = [[0,1],[0,2],[3,4],[2,3]]
g = Graph(n)
g.makeGraph(connections)
print("Minimum Number of wires to make the connection are {}".format(g.minimumWireToMakeConnections()))
