 # Problem Statement : https://www.geeksforgeeks.org/check-if-a-given-graph-is-bipartite-using-dfs/
def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def DFS(graph,vertex,visited,color):

    # Check for each neighbour vertex.
    for nbh in graph[vertex]:
        if not visited[nbh]:
            # If adjacent vertex is not visited then visit this and assign color opposite of parent vertex.
            visited[nbh] = True
            color[nbh] = 1 - color[vertex]

            # Call DFS recursively for child nodes.
            if not DFS(graph,nbh,visited,color):
                return False

        # If neighbour vertex is already visited then check that it's color is different from parent vertex.
        elif color[nbh] == color[vertex]:
            return False

    return True

# TC = O(N) SC = O(N)
def check_Bipartite_DFS(graph,N):

    # To keep a check on whether vertex visited or not.
    visited = [0 for i in range(N + 1)]

    # To color the vertices of graph with 2 color
    color = [0 for i in range(N + 1)]

    # This for loop will check for each unvisited vertex , in case of disconnected graph.
    for vertex in range(1,N+1):
        if visited[vertex] == False:

            # If vertex is unvisited then visit this vertex and mark it as True and assign initial color as 1.
            visited[vertex] = True
            color[vertex] = 1

            # If any of the recursive call return False then return false.
            if not DFS(graph,vertex,visited,color):
                return False

    return True



# Driver Code

# No of nodes
N = 6

# To maintain the adjacency list of graph
adj = [[] for i in range(N + 1)]

# Adding edges to the graph
addEdge(adj, 1, 2)
addEdge(adj, 2, 3)
addEdge(adj, 3, 4)
addEdge(adj, 4, 5)
addEdge(adj, 5, 6)
addEdge(adj, 6, 1)


if check_Bipartite_DFS(adj,N):
    print("Given Graph is Bipartite")
else:
    print("Given Graph is not bipartite")