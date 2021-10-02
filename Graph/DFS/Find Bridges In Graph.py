# Problem Bridges in the Graph
# Video Solution : https://www.youtube.com/watch?v=ECKTyseo2H8
from collections import defaultdict
class Graph(object):

    def __init__(self,V):
        self.V = V
        self.graph = defaultdict(list)
        self.Timer = 0

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def makeGraph(self,edges):
        for u,v in edges:
            self.addEdge(u,v)

    def dfs(self,node,visited,parent,inTime,low):

        # Mark this current node as visited.
        visited[node] = True

        # Assign the Distance & Low value to this node.
        inTime[node] = low[node] = self.Timer
        self.Timer = self.Timer + 1

        # Now Traverse all it's adjacent Node.
        for child in self.graph[node]:

            # If Child is the Parent of the given node.
            if child == parent:
                continue

            # If Child is already visited  then it means this edge is a Bak Edge( Node is Connected to it's Ancestor )
            # In this Case we minimise the Low time of Current Node.
            if visited[child] == True:

                low[node] = min(low[node],inTime[child])

            # This is a forward edge , so make DFS call for this child node keeping current node as it's parent.
            else:
                self.dfs(child,visited,node,inTime,low)

                # Now check if the Low time of child is greater than InTime of current node, if it is then we can say that this edge is a Bridge.
                if  low[child] > inTime[node]:
                    print("%d %d" % (node, child))


                # Now Try to low the low Time of the given current Node.
                low[node]  = min(low[node],low[child])



    # TC = O(V+E) As we are doing Simple DFS.
    # SC = O(V) + O(V) + O(V) = O(V)
    def findBridges(self):

        visited = [False] * (self.V)
        inTime = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)

        for i in range(self.V):
            if visited[i] == False:
                self.dfs(i,visited,-1,inTime,low)



# Driver Code
g1 = Graph(5)
edges1 = [[1,0],[0,2],[2,1],[0,3],[3,4]]
g1.makeGraph(edges1)

print("Bridges in the First Graph")
g1.findBridges()


g2 = Graph(4)
edges2 = [[0,1],[1,2],[2,3]]
g2.makeGraph(edges2)

print("Bridges in the Second Graph")
g2.findBridges()

g3 = Graph(7)
edges3 = [[0,1],[1,2],[2,0],[1,3],[1,4],[1,6],[3,5],[4,5]]
g3.makeGraph(edges3)
print("Bridges in the Third Graph")
g3.findBridges()