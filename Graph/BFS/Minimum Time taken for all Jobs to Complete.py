# Problem Statement : https://www.geeksforgeeks.org/minimum-time-taken-by-each-job-to-be-completed-given-by-a-directed-acyclic-graph/
from collections import defaultdict

class Graph(object):

    def __init__(self,vertices,edge):
        self.graph = defaultdict(list)
        self.V = vertices
        self.edges = edge

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def makeGraph(self):
        self.addEdge(1, 3)
        self.addEdge(1, 4)
        self.addEdge(1, 5)
        self.addEdge(2, 3)
        self.addEdge(2, 8)
        self.addEdge(2, 9)
        self.addEdge(3, 6)
        self.addEdge(4, 6)
        self.addEdge(4, 8)
        self.addEdge(5, 8)
        self.addEdge(6, 7)
        self.addEdge(7, 8)
        self.addEdge(8, 10)

    # Function to find the minimum time needed by each node to get the task.
    # TC = O(V+E)
    # SC = O(V)
    def printOrder(self,n,m):

        # Create an indegree array to store the in degrees of the vertices.
        indegree = [0]*(n+1)

        # Traverse the graph and count the indegree of each nodes . It will take O(V+E).
        for i in self.graph:
            for j in self.graph[i]:
                indegree[j] += 1

        # Create an array to store time for each Job.
        job = [0]*(self.V+1)

        # Create the Queue and store all the Vertices with 0 indegree.
        Q = []
        for i in range(1,n+1):
            if indegree[i] == 0:
                Q.append(i)
                job[i] = 1

        while Q:

            v = Q.pop(0) # Pop the Node and decrease the indegree of  each adjacent node of popped node.

            for adj in self.graph[v]:
                indegree[adj] = indegree[adj] - 1

                # If in degree becomes 0 then add this adjacent node in the Queue and time taken bt this Job will be 1+ time by parent Job.
                if indegree[adj] == 0:
                    job[adj] = 1 + job[v]
                    Q.append(adj)

        # Print the Time taken by each job to complete.
        for i in range(1,n+1):
            print(job[i],end=' ')
        print()

# Driver Code
vertex = 10
edges = 13

g = Graph(vertex,edges)
g.makeGraph()
g.printOrder(vertex,edges)
