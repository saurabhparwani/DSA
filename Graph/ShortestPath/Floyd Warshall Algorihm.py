# Problem Link : https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/

# Define Infinite variable for a graph.
INF = 99999

def printSolution(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            print(graph[i][j],end = ' ')
        print()

    print()

# TC = O(V*V*V)
# SC = O(1)
def floydWarshall(graph):

    V = len(graph)
    # Create a copy Graph
    distance = [[0 for i in range(V)] for j in range(V)]
    for i in range(len(graph)):
        for j in range(len(graph)):
            distance[i][j] = graph[i][j]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                # First check that whether element is not a diagonal element.
                
                distance[i][j] = min(distance[i][j],distance[i][k]+distance[k][j])

    printSolution(distance)



# Driver Code

graph = [
         [0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
]

floydWarshall(graph)