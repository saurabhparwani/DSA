from collections import defaultdict

class Graph(object):

    def __init__(self,vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def isCyclicUtility(self,node,visited,rec_array):

        visited[node] = True
        rec_array[node] = True

        for neighbour in self.graph[node]:

            if visited[neighbour] == False:
                if self.isCyclicUtility(neighbour,visited,rec_array):
                    return True

            elif rec_array[neighbour] == True:
                return True

        rec_array[node] = False
        return False

    def isCyclic(self):

        visited = [False]*(self.V+1)
        rec_array = [False] * (self.V+1)

        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtility(node,visited,rec_array):
                    return True

        return False

# Complexity Analysis:
# Time Complexity: O(V+E).
# Time Complexity of this method is same as time complexity of DFS traversal which is O(V+E).
# Space Complexity: O(V).
# To store the visited and recursion stack O(V) space is needed.



# Driver Code
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.isCyclic() == 1:
    print ("Graph has a cycle")
else:
    print ("Graph has no cycle")