# Problem Statement : https://www.geeksforgeeks.org/find-if-there-is-a-path-of-more-than-k-length-from-a-source/
from collections import  defaultdict
class Node(object):
    def __init__(self,node,weight):
        self.node = node
        self.weight = weight

class Graph(object):
    def __init__(self,V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self,u,v,w):
        self.graph[u].append(Node(v,w))
        self.graph[v].append(Node(u,w))

    def makeGraph(self):
        self.addEdge(0, 1, 4)
        self.addEdge(0, 7, 8)
        self.addEdge(1, 2, 8)
        self.addEdge(1, 7, 11)
        self.addEdge(2, 3, 7)
        self.addEdge(2, 8, 2)
        self.addEdge(2, 5, 4)
        self.addEdge(3, 4, 9)
        self.addEdge(3, 5, 14)
        self.addEdge(4, 5, 10)
        self.addEdge(5, 6, 2)
        self.addEdge(6, 7, 1)
        self.addEdge(6, 8, 6)
        self.addEdge(7, 8, 7)


    # TC = O(N!) Bcoz we are traversing through all possible paths in the graph.
    # SC = O(N) For storing the visited array.
    def findPathUtiity(self,node,k,path,visited):
        if k <= 0:
            path.append(node)
            visited[node] = True
            print(path)
            return True

        visited[node] = True
        path.append(node)

        for nbh in self.graph[node]:
            if visited[nbh.node] == False:
                if self.findPathUtiity(nbh.node,k-nbh.weight,path,visited):
                    return True

        visited[node] = False
        path.pop()
        return False

    def findkPath(self,src,k):

        visited = [False]*(self.V+1)
        path = []
        return self.findPathUtiity(src,k,path,visited)


# Driver Code
V = 9
g = Graph(V)
g.makeGraph()

src = 0
k = 62

if g.findkPath(src,k):
    print("Path Found")
else:
    print("Path Not Found")