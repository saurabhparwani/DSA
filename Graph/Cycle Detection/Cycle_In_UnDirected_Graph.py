from collections import defaultdict
from collections import deque
# This class represents a directed graph
# using adjacency list representation
class Graph(object):

    # Constructor
    def __init__(self,vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    # Function to add an Edge in graph
    def addEdge(self,u,v):

        # Create and Undirected Graph , that's why both the nodes will connect each other
        self.graph[u].append(v)

        self.graph[v].append(u)

    def buildGraph(self):
        self.addEdge(1, 0)
        self.addEdge(1, 2)
        self.addEdge(2, 0)
        self.addEdge(0, 3)
        self.addEdge(3, 4)

    # Utility Method to DO DFS on each node and check if cycle exist or not
    # It will check that adjacent node which is already visited is Parent of found node or not.
    # If it is not the Parent then there is a cycle.
    def isCyclicDFSUtility(self,source,visited,parent):

        # Mark Sorce node Visited
        visited[source] =  True

        # Traverse Through each neighbour of source and then call DFS for each Unvisited vertex
        for i in self.graph[source]:

            # To Call IsCyclic Method for each Unvisited Vertex
            if visited[i] == False:
                if self.isCyclicDFSUtility(i,visited,source):
                    return True

             # To check that neighbour node is parent or not
            elif parent!=i:
                return True
        return False


    # This Method will iterate through each unvisited vertex of graph and
    # it will use helper method which will be using DFS to perform Traversing.

    # Time Complexity: O(V+E).
    # The program does a simple DFS Traversal of the graph which is represented using adjacency list. So the time complexity is O(V+E).

    # Space Complexity: O(V).
    # To store the visited array O(V) space is required.
    def isCyclic_Using_DFS(self):

        # To get total number of Vertex
        number_of_vertex = self.V
        # Created the Visited Array and Initialize with False
        visited = [False]*number_of_vertex

        for i in range(number_of_vertex):
            if visited[i] == False:

                # To Call Utility Method for Each Unvisited vertex and if cycle exist then it will simply return True
                if (self.isCyclicDFSUtility(i,visited,-1)):
                    return  True

        # Return False is Cycle does not Present
        return False


     # Utility Method to Perform BFS from a given source Vertex . This method will keep track of Parent Node.
    def cycle_BFS_Utility(self,vertex,visited):

        # Create a Parent Array to Store Parent
        parent = [-1]*self.V

        que = deque()
        que.append(vertex)
        visited[vertex] = True

        # Loop till Queue is not Empty

        while que:
            # Pop the node from queue
            u = que.pop()

            # Get All the Adjacent node in the Queue if they are not visited
            # and if they are already visited then check adjacent node is parent or not
            # if it is not parent then cycle exist

            for v in self.graph[u]:
               # If adjacent node is not visited
               if visited[v] == False:
                   visited[v] = True
                   que.append(v)
                   parent[v] = u

               # Check for Parent Condition
               elif parent[u] != v:
                   return True

        return False

    # Method to Check Cycle in a graph using BFS method .
    # This Method will use a helper Utility method which will do BFS and track Parent of each visited node.
    # For every visited vertex ‘v’, if there is an adjacent ‘u’ such that u is already visited and u is not a parent of v, then there is a cycle in the graph.
    # If we don’t find such an adjacent for any vertex, we say that there is no cycle.

    # Time Complexity  : The program does a simple BFS Traversal of graph and graph is represented using adjacency list. So the time complexity is O(V+E)
    # Space Complexity : 0(N) for storing the Vertex of Graph in Queue where N is the number of vertex in graph.

    def is_Cyclic_using_BFS(self):
        number_of_vertex = self.V

        # Create a Visited Array to track visited nodes
        visited = [False] * number_of_vertex

        for i in range(number_of_vertex):
            if visited[i] == False:
                if self.cycle_BFS_Utility(i,visited):
                    return True
        return False


g = Graph(5)
g.buildGraph()

g1 = Graph(3)
g1.addEdge(0,1)
g1.addEdge(1,2)

# Check for First  Graph  Using DFS Method
if g.isCyclic_Using_DFS():
    print("Graph is Cyclic")
else:
    print("Graph is not cyclic")

# Check for First  Graph  Using BFS Method
if g.is_Cyclic_using_BFS():
    print("Graph is Cyclic")
else:
    print("Graph is not cyclic")


# Check for Second Graph  Using DFS Method
if g1.isCyclic_Using_DFS():
    print("Graph is Cyclic")
else:
    print("Graph is not cyclic")

# Check for Second Graph  Using DFS Method
if g1.is_Cyclic_using_BFS():
    print("Graph is Cyclic")
else:
    print("Graph is not cyclic")