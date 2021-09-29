# Problem Solution :  https://www.hackerrank.com/challenges/journey-to-the-moon/problem
# Video Solution : https://www.youtube.com/watch?v=IM1xOjamHA8&t=736
from collections import  defaultdict

class Graph(object):
    def __init__(self,V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def makeGraph(self,edges):
        for edge in edges:
            self.addEdge(edge[0],edge[1])
            self.addEdge(edge[1],edge[0])

    def dfsUtility(self,src,visited,counter):

        visited[src] = True
        counter[0] += 1
        for nbh in self.graph[src]:
            if visited[nbh] == False:
                self.dfsUtility(nbh,visited,counter)

    # TC = O(V+E) As we are doing simple DFS in the graph.
    # SC = O(V+V+V) For Recursion , For Visited array , For Components list.
    def validPairs(self):
        components = []  # List to store the number of vertices in the graph components.
        visited = [False] * (self.V+1)

        # Do the DFS traversal and make the components list which will store the number of vertices in different sub graphs.
        # For each sub graph counter will be 0 and it will count the total no of vertices in that sub graph and finally it will append
        # that count in component list.
        for src in range(len(self.graph)):
            if visited[src] == False:
                counter = [0]
                self.dfsUtility(src,visited,counter)
                components.append(counter[0])

        # Count the total number of possible Astronaut combination by formulae nC2 = (n*(n-1))/2
        total_combination = (self.V *(self.V - 1)) // 2

        # Now subtract all the other combination which can be made by that components array.
        for comp in components:
            count = (comp*(comp-1))//2
            total_combination = total_combination - count

        return total_combination

# Driver Code
vertex = 4
pairs = 1
edges = [[0,2]]

graph = Graph(vertex)
graph.makeGraph(edges)

print("Number of valid pairs in the graph {}".format(graph.validPairs()))
