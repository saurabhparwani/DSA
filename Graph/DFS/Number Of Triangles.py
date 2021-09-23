# Problem Statement : https://www.geeksforgeeks.org/number-of-triangles-in-directed-and-undirected-graphs/

# We will check that whether is there any triplet such that (i,j,k) where i != j && j!= k and there exist a edge b/w i->j , j->k , k->i.
# For an Undirected graph such combination will give 6 triangles , so we will divide total triangles by 6 for Undirected graph.
# For an directed graph such combination will give 3 triangles , so we will divide total triangles by 3 for Directed graph.

# TC = O(V*V*V) for 3 Loops.
# SC = O(1)
def countTriangle(graph,isDirected):

    total_triangles = 0

    v = len(graph)

    for i in range(v):
        for j in range(v):
            for k in range(v):
                # Apply the Condition  here. If the Condition satisfies simple increase the total triangle count in the graph.
                if i!=j and j!=k and k!=i and graph[i][j] and graph[j][k] and graph[k][i]:
                    total_triangles += 1

    if isDirected:  # If graph is Directed then divide the triangles by 3 else 6.
        total_triangles = total_triangles//3
    else:
        total_triangles = total_triangles//6

    return total_triangles

# Driver Code

undirected_graph = [[0, 1, 1, 0],[1, 0, 1, 1], [1, 1, 0, 1],[0, 1, 1, 0]]

directed_graph = [[0, 0, 1, 0],[1, 0, 0, 1], [0, 1, 0, 0],[0, 0, 1, 0]]

print("Number of Triangles in the undirected graph are {}".format(countTriangle(undirected_graph,False)))

print("Number of Triangles in the Directed graph are {}".format(countTriangle(directed_graph,True)))