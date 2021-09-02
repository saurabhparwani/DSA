# Problem Statement :  https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/

class Graph(object):

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def makeGraph(self):
        self.addEdge(1, 0)
        self.addEdge(2, 1)
        self.addEdge(3, 4)

    # Utility DFS Method for DFS. This will mark the current vertex as visited and add that vertex in list.
    # And then it will traverse for each unvisited neighbour of that vertex.
    # Finally it will return the list which will contain all vertex in one dfs call.
    def dfsUtility(self,vertex,visited,temp):

        visited[vertex]  = True
        temp.append(vertex)

        for neighbour in self.adj[vertex]:
            if visited[neighbour] == False:

                # Update the temp list with returned list.
                temp = self.dfsUtility(neighbour,visited,temp)

        return temp


    # Method to find the Number of connected components in a undirected graph.
    # This method is using DFS although we can do this via BFS as well.
    # TC = Time complexity of above solution is O(V + E) as it does simple DFS for given graph.
    # SC = O(V) For Unvisited array. O(V) For the Stack space for DFS . So Overall O(V)
    def connectedComponents(self):

        visited = [False] * (self.V)
        connected_comp = []

        # Loop through all Unvisited in case of disconnected graph.
        for vertex in range(self.V):
            # If vertex is unvisited then  create a new list of components and apply dfs from that vertex.
            if visited[vertex] == False:
                temp = []

                # Update the temp list with the list returned by DFS method.
                temp = self.dfsUtility(vertex,visited,temp)

                # Add this list into the final Connected components list.
                connected_comp.append(temp)

        # Return the final CC list.
        return connected_comp


# Driver Code
graph = Graph(5)
graph.makeGraph()

connected_comp = graph.connectedComponents()
print("Following are the connected components in the Graph")
for comp in connected_comp:
    print(comp)