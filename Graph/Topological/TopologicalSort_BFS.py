# Problem Statement :  https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
# Alternate Problem : Kahn's Algorithm or Detect Cycle in directed graph by using BFS.
from collections import  defaultdict
class Graph(object):

    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def topologicalSort(self):

        # Create a vector to store indegrees of all
        # vertices. Initialize all indegrees as 0.
        indegree = [0] * (self.V)

        # Traverse adjacency lists to fill indegrees of
        # vertices.  This step takes O(V + E) time
        for i in self.graph:
            for j in self.graph[i]:
                indegree[j] += 1

        # Create an queue and enqueue all vertices with
        # indegree 0
        queue = []
        count = 0
        topological_order = []
        for i in range(self.V):
            if indegree[i] == 0:
                queue.append(i)

        # One by one dequeue vertices from queue and enqueue
        # adjacents if indegree of adjacent becomes 0
        while queue:
            # Extract front of queue (or perform dequeue)
            # and add it to topological order
            u = queue.pop(0)
            topological_order.append(u)

            # Iterate through all neighbouring nodes
            # of dequeued node u and decrease their in-degree by 1
            for v in self.graph[u]:
                indegree[v]-=1
                # If in-degree becomes zero, add it to queue
                if indegree[v] == 0:
                    queue.append(v)

            count += 1

        if count != self.V:
            print("There is a cycle in the graph")
        else:
            print("Topological sort of the graph is ")
            print(topological_order)

# Time Complexity: O(V+E).
# The outer for loop will be executed V number of times and the inner for loop will be executed E number of times.
# Auxillary Space: O(V).
# The queue needs to store all the vertices of the graph. So the space required is O(V)


# Driver Code
g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

g.topologicalSort()