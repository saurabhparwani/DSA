# Problem Statement :  https://www.techiedelight.com/bipartite-graph/

from collections import deque

# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, N):
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(N+1)]
        # add edges to the undirected graph
        for (src, dest) in edges:
            # add an edge from source to destination
            self.adjList[src].append(dest)

            # add an edge from destination to source
            self.adjList[dest].append(src)


# 1 for Blue Color , 0 for red color
def check_BiPartite_Using_BFS(graph,vertex,visited,color_arr):

    # Mark the Current Vertex as visited & assign first vertex color 1 i.e Blue.
    visited[vertex] = True
    color_arr[vertex] = 1

    # Append the current vertex in the Queue.
    que = deque()
    que.append(vertex)

    # Traverse while queue is not empty.
    while que:
        # Pop the vertex from queue and go through all it's adjacent vertices.
        u = que.popleft()

        for v in graph.adjList[u]:
            # If vertex is not visited then mark as visited and append in queue and also assign different color than it's parent.
            if visited[v] == False:
                visited[v] = True
                color_arr[v] = 1 - color_arr[u]
                que.append(v)

            # If vertex is already visited then check that it's color is not same it's parent.
            elif color_arr[v] == color_arr[u]:
                return False
    return True


# TC = O(E+V) If Graph is represented as Adjacency list , O(V*V) If graph is represented as Matrix.
# Space Complexity : O(V) for Queue , and O(V+E) for storing the graph vertex & edges in form of adjacency list.
def checkBipartite(graph,N):

    visited = [False]* (N+1)
    color_arr = [-1] * (N+1)

    # Check for each unvisited vertex in case of disconnected graph.
    for i in range(1,N+1):
        if visited[i] == False:
            if not check_BiPartite_Using_BFS(graph,i,visited,color_arr):
                return False

    return True

# Driver Code

# List of graph edges as per the above diagram.
# Note that if we add edge `2 —> 4`, the graph becomes non-bipartite
edges = [(1, 2), (2, 3), (2, 8), (3, 4), (4, 6), (5, 7), (5, 9), (8, 9)]

# total number of nodes in the graph
N = 10

# build a graph from the given edges
graph = Graph(edges, N)

# Perform BFS traversal starting from vertex 1
if checkBipartite(graph,N):
    print("Graph is Bipartite")
else:
    print("Graph is not Bipartite")
