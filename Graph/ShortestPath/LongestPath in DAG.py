# Problem Statement : https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/
from collections import  defaultdict
import  heapq
class Node(object):
    def __init__(self,node,weight):
        self.node = node
        self.weight = weight

    def __str__(self):
        self.node

class Graph(object):
    def __init__(self,V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self,u,v,w):
        self.graph[u].append(Node(v,w))

    def makeGraph(self):
        self.addEdge(0,1,5)
        self.addEdge(0,2,3)
        self.addEdge(1,3,6)
        self.addEdge(1,2,2)
        self.addEdge(2,4,4)
        self.addEdge(2,5,2)
        self.addEdge(2,3,7)
        self.addEdge(3,5,1)
        self.addEdge(3,4,-1)
        self.addEdge(4,5,-2)

    # TC = O(V+ELOgV) == O(ELogV) As it is same as Dijkstra's Algorithm.
    # SC = O(V) For Priority Queues.
    def longestPathinDirectedGraph(self,src):

        distances = [float("-Inf")] *(self.V)

        pq = []
        distances[src] = 0
        heapq.heappush(pq,(src,0))
        while len(pq) !=0:
            curr_node , curr_dist = heapq.heappop(pq)
            for nbh in self.graph[curr_node]:
                distance = curr_dist + nbh.weight
                if distance > distances[nbh.node]:
                    distances[nbh.node] = distance
                    heapq.heappush(pq,(nbh.node,distance))

        print(distances)

#
# Driver Code
g = Graph(6)
g.makeGraph()
print("Distance of vertices from 1 is ")
g.longestPathinDirectedGraph(1)