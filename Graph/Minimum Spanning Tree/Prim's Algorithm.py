# Problem Statement  : https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/
# Solution Prim's Algorithm : https://www.youtube.com/watch?v=HnD676J56ak&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=20
from collections import defaultdict
import heapq

class Node(object):

    def __init__(self,vertex,weight):
        self.vertex = vertex
        self.weight = weight

    def getVertex(self):
        return self.vertex

    def getWeight(self):
        return self.weight

    def __lt__(self, other):
        return ((self.weight < other.weight))

class Graph(object):

    def __init__(self,vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    def addEdge(self,src,dest,weight):

        self.graph[src].append(Node(dest,weight))
        self.graph[dest].append(Node(src,weight))

    def makeGraph(self):
        # self.addEdge(0, 1, 4)
        # self.addEdge(0, 7, 8)
        # self.addEdge(1, 2, 8)
        # self.addEdge(1, 7, 11)
        # self.addEdge(2, 3, 7)
        # self.addEdge(2, 8, 2)
        # self.addEdge(2, 5, 4)
        # self.addEdge(3, 4, 9)
        # self.addEdge(3, 5, 14)
        # self.addEdge(4, 5, 10)
        # self.addEdge(5, 6, 2)
        # self.addEdge(6, 7, 1)
        # self.addEdge(6, 8, 6)
        # self.addEdge(7, 8, 7)

        self.addEdge(0, 1, 2)
        self.addEdge(1, 2, 3)
        self.addEdge(0, 3, 6)
        self.addEdge(1, 3, 8)
        self.addEdge(1, 4, 5)
        self.addEdge(2, 4, 7)

    def primsAlgorithm(self):
        V = self.V
        key = [100000] * V
        mstSet = [False] * V
        parent = [-1]*V

        key[0] = 0
        parent[0] = -1

        pq = []
        heapq.heappush(pq, Node(key[0], 0))

        while len(pq):
            vertex = heapq.heappop(pq).getVertex()
            mstSet[vertex] = True

            for nodes in self.graph[vertex]:
                if mstSet[nodes.getVertex()] == False and  nodes.getWeight() < key[nodes.getVertex()]:
                    parent[nodes.getVertex()] = vertex
                    key[nodes.getVertex()] = nodes.getWeight()
                    heapq.heappush(pq, Node(nodes.getVertex(), key[nodes.getVertex()]))


        for i in range(1,V):
            print("{} --- {}".format(parent[i],i))




# Time Complexity: The time complexity of the above code/algorithm looks O(V^2) as there are two nested while loops.
# If we take a closer look, we can observe that the statements in inner loop are executed O(V+E) times (similar to BFS).
# The inner loop has decreaseKey() operation which takes O(LogV) time. So overall time complexity is O(E+V)*O(LogV)
# which is O((E+V)*LogV) = O(ELogV) (For a connected graph, V = O(E))

 # Driver Code
graph = Graph(5)
graph.makeGraph()
graph.primsAlgorithm()