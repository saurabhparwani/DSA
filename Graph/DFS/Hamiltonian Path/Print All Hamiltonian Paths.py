# Problem Statement : https://www.techiedelight.com/print-all-hamiltonian-path-present-in-a-graph/

class Graph(object):
    def __init__(self,edges,N):
        self.adjList = [[] for _ in range(N)]
        # Add edges to the Undirected Graph.

        for (src,dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def printAllHamiltonianPaths(g, v, visited, path, N):

    # If length of the Path is equal to the total number of N then Simply print that path.
    if len(path) == N:
        print(path)
        return

    # Check if every edge starting from vertex `v` leads to a solution or not
    for nbh in g.adjList[v]:
        if visited[nbh] == False:

            visited[nbh] = True
            path.append(nbh)

            printAllHamiltonianPaths(g,nbh,visited,path,N)

            visited[nbh] = False
            path.pop()

# Driver Code

# consider a complete graph having 4 vertices
edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

# total number of nodes in the graph
N = 4

# build a graph from the given edges
g = Graph(edges, N)

# starting node
start = 0

# add starting node to the path
path = [start]

# mark the start node as visited
visited = [False] * N
visited[start] = True

printAllHamiltonianPaths(g, start, visited, path, N)

