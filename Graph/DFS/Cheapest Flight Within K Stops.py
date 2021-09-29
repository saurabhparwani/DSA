# Problem Statement : https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
# Optimized Answer : https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/786407/Python-Dijkstra-Solution-faster-than-89
# Optimized Answer : https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/738656/Python3-BFS-with-explanation-and-comments
from collections import deque, defaultdict
class Node(object):
    def __init__(self,node,weight):
        self.node = node
        self.weight = weight

class Graph(object):
    def __init__(self,n):
        self.V = n
        self.graph = defaultdict(list)

    def addEdge(self,u,v,w):
        self.graph[u].append(Node(v,w))

    def makeGraph(self,flights):
        for flight in flights:
            self.addEdge(flight[0],flight[1],flight[2])

    def dfsUtility(self,src,dst,k,fare,cheapestFare,visited):

        # Base Case , If k < -1 then we can not explore more Nodes.
        if k < -1:
            return

        # If we reached at the destination then we will update the cheapestFare if it's less than existing cheapest fare.
        if src == dst:
            cheapestFare[0] = min(fare,cheapestFare[0])
            return

        # Else We will visited this current node and we will explore all other unvisited nodes keeping in mind that
        # fare should be less than existing found cheapest fare.
        visited[src] = True

        for nbh in self.graph[src]:
            if visited[nbh.node] == False and (fare + nbh.weight < cheapestFare[0]):
                self.dfsUtility(nbh.node,dst,k-1,fare+nbh.weight,cheapestFare,visited)

        # BackTrack to mark visited node again unvisited
        visited[src] = False

    # Using DFS + Pruning , Not much efficient .
    # TC = O(V+E) For Sparse Graph , O(E.V*V) For Dense Graph
    def findChepestPath(self,src,dst,k):
        visited = [False] * (self.V + 1)
        cheapestFare = [10000000]
        self.dfsUtility(src,dst,k,0,cheapestFare,visited,)

        if cheapestFare[0] == 10000000:
            return -1
        else:
            return cheapestFare[0]

# TC = O(V+E)
# SC = O(V) For Queue + Visited Map.
def findCheapestPriceUsingBFS(n,flights,src,dst,k):
    graph = defaultdict(list)

    for srcc,dest,price in flights:
        graph[srcc].append([dest,price])
    visited = {src:0}
    queue = deque([(src,0,0)])
    while queue:
        # Pop the Current data from the Queue.
        city,currPrice,stops = queue.popleft()

        # Add if the NewCity is not visited or cost to visit the newCIty is less than existing cost.
        for newcity, cost in graph[city]:

            if newcity not in visited or currPrice + cost < visited[newcity]:

                # Add in Queue only when stops are lesser than given K.
                if stops < k:
                    queue.append((newcity,currPrice+cost,stops+1))

                visited[newcity] = currPrice + cost
    if dst in visited:
        return visited[dst]
    else:return -1



# Driver Code
n = 5
flights = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
src = 2
dst = 1
k = 1
g = Graph(n)
g.makeGraph(flights)

cheapestFare = g.findChepestPath(src,dst,k)
print("Cheapest Fare {}".format(cheapestFare))

cheapestFare2 = findCheapestPriceUsingBFS(n,flights,src,dst,k)
print(cheapestFare2)

