# Problem Statement :  https://www.geeksforgeeks.org/strongly-connected-components/
from collections import defaultdict

class Graph(object):

    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Method to store the vertex in the stack based upon their finishing time.
    # It will simply do the DFS and once the dfs ends it will add that vertex into the stack and then return that stack.
    def fillStack(self,stack,visited,vertex):

        # Mark the current vertex as visited.
        visited[vertex] = True
        # Traverse all it's connected  vertex and if any of the vertex is unvisited then call DFS for that neighbour.
        for neighbour in self.graph[vertex]:
            if visited[neighbour] == False:
                self.fillStack(stack,visited,neighbour)

        # Once DFS is complete for all the unvisited neighbour then append the vertex into the stack.
        stack.append(vertex)


    # Method to return the transpose of the graph.
    # This method will simply reverse the all edges.
    def getTransposegraph(self):

        tp_graph = Graph(self.V)
        # Recur for all the vertices adjacent to this vertex
        for i in range(self.V):
            for j in self.graph[i]:
                tp_graph.addEdge(j,i)

        return tp_graph

    def dfsUtil(self,vertex,visited):
        # Mark the current node as visited and print it
        visited[vertex] = True
        print(vertex,end = "  ")
        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[vertex]:
            if visited[neighbour] == False:
                self.dfsUtil(neighbour,visited)

    # Time Complexity: The above algorithm calls DFS, finds reverse of the graph and again calls DFS.
    # DFS takes O(V+E) for a graph represented using adjacency list.
    # Reversing a graph also takes O(V+E) time. For reversing the graph, we simple traverse all adjacency lists.

    # Space Complexity : O(V) for Stack , O(E+V) For creating the transpose graph, O(V) For recursion stack.
    def printSSC(self):

        visited = [False] * (self.V)

        stack = []

        # Fill the stack based upon their finishing time.
        for i in range(self.V):
            if visited[i] == False:
                self.fillStack(stack,visited,i)

        # Create a transpose Graph
        transpose_graph = self.getTransposegraph()
        # Mark all the vertices as not visited (For second DFS)
        visited = [False] * (self.V)

        # Now process all vertices in order defined by Stack
        while stack:
            vertex = stack.pop()
            if visited[vertex] == False:
                transpose_graph.dfsUtil(vertex,visited)
                print()


# Driver Code

# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

print("Strongly connected components of the given graphs are")

g.printSSC()

