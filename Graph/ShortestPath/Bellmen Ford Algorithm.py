# Problem Statement : https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/

class Graph(object):
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def makeGraph(self):
        self.addEdge(0, 1, -1)
        self.addEdge(0, 2, 4)
        self.addEdge(1, 2, 3)
        self.addEdge(1, 3, 2)
        self.addEdge(1, 4, 2)
        self.addEdge(3, 2, 5)
        self.addEdge(3, 1, 1)
        self.addEdge(4, 3, -3)

    def printArr(self,dist):
        print("Vertex distance from source")
        for  i in range(self.vertices):
            print("{0}\t\t{1}".format(i, dist[i]))


    # TC = O(V*E)
    # SC = O(V) for distance Array.
    def BellmanFord(self,src):

        # Step 1 : Initialize distances from src to all other vertices as INFINITE
        distance = [float("Inf")] * self.vertices
        distance[src] = 0

        # Relax all edges |V| - 1 times. A simple shortest path from src to any other vertex can have at-most |V| - 1 edges
        for _ in range(self.vertices):
            for u,v,w in self.graph:
                if distance[u]!= float("Inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        # Now Relax for 1 more time and if now distance further reduces then it means Negative Cycle is present.
        for u,v,w in self.graph:
            if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                print("Graph Has Negative Cycle")
                return

        # If Graph does not have any negative cycle then simply print  the distance array.
        self.printArr(distance)



# Driver Code

g = Graph(5)
g.makeGraph()
g.BellmanFord(0)
