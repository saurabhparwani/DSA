from collections import defaultdict
# This class represents a directed graph
# using adjacency list representation
class Graph(object):

    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    # Function to add an Edge in graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def buildGraph(self):
        self.addEdge(0, 1)
        self.addEdge(0, 2)
        self.addEdge(1, 2)
        self.addEdge(2, 0)
        self.addEdge(2, 3)
        self.addEdge(3, 3)

    def BFS(self,source):
        visited=[False]*(max(self.graph)+1)
        queue=[]
        queue.append(source)
        visited[source]=True

        while queue:
            # Dequeue a vertex from
            # queue and print it
            s=queue.pop(0)
            print(s,end=" ")
            #Get all adjacent vertices of the  # dequeued vertex s. If a adjacent
            #  has not been visited, then mark it # visited and enqueue it
            for neighbour in self.graph[s]:
                if visited[neighbour] == False:
                    queue.append(neighbour)
                    visited[neighbour]=True


g =Graph()
g.buildGraph()
g.BFS(2)


# Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.



