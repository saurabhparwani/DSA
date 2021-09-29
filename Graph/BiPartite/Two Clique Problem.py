# Problem Statement : https://www.geeksforgeeks.org/two-clique-problem-check-graph-can-divided-two-cliques/
from queue import Queue

# TC = O(V*V)
# SC = O(V)
def isBipartiteUtil(G, src, colorArr):

    global V
    colorArr[src] = 1
    # Create a queue (FIFO) of vertex numbers
    # and enqueue source vertex for BFS traversal
    q = Queue()
    q.put(src)

    while not q.empty():
        # Dequeue a vertex from queue
        u = q.get()

        # Find all non-colored adjacent vertices
        for v in range(V):

            # An edge from u to v exists and destination v is not colored
            if (G[u][v] and colorArr[v] == -1):
                # Assign alternate color to this adjacent v of u
                colorArr[v] = 1 - colorArr[u]
                q.put(v)

            # An edge from u to v exists and destination v is colored with same color as u
            elif (G[u][v] and colorArr[v] == colorArr[u]):
                return False

    # If we reach here, then all adjacent vertices can be colored with alternate color
    return True

def isBipartite(G):
    global V
    colorArr = [-1] * V

    # One by one check all not yet colored vertices. In case of dis connected graph.
    for i in range(V):
        if (colorArr[i] == -1):
            if (isBipartiteUtil(G, i, colorArr) == False):
                return False
    return True


def canBeDividedinTwoCliques(G):
    global V

    # Find complement of G[][] All values are complemented except diagonal ones
    GC = [[None] * V for i in range(V)]
    for i in range(V):
        for j in range(V):
            GC[i][j] = not G[i][j] if i != j else 0

    # Return true if complement is Bipartite else false.
    return isBipartite(GC)


# Driver Code
V = 5
G = [[0, 1, 1, 1, 0],
     [1, 0, 1, 0, 0],
     [1, 1, 0, 0, 0],
     [0, 1, 0, 0, 1],
     [0, 0, 0, 1, 0]]

if canBeDividedinTwoCliques(G):
    print("Yes")
else:
    print("No")