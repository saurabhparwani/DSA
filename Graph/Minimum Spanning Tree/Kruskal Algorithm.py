# Problem Statements : https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i(uses path compression technique)
    def find(self,parent,i):
         if parent[i] != i:
            parent[i] = self.find(parent,parent[i])

         return parent[i]

    # A function that does union of two sets of x and y (uses union by rank)
    def union(self,parent,rank,x,y):
        xroot = self.find(parent,x)
        yroot = self.find(parent,y)

        # Attach smaller rank tree under root of high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[yroot] < rank[xroot]:
            parent[yroot] = xroot

        # If ranks are same, then make one as root and increment its rank by one
        else:
            parent[xroot] = yroot
            rank[yroot] += 1

    # TC: O(ELogE) or O(ELogV) Sorting of edges takes O(ELogE) time.
    # After sorting, we iterate through all edges and apply the find-union algorithm.
    # The find and union operations can take at most O(LogV) time.
    # So overall complexity is O(ELogE + ELogV) time. The value of E can be at most O(V2), so O(LogV) is O(LogE) the same.
    # Therefore, the overall time complexity is O(E logE) or O(E logV)
    def kruskalAlgo(self):

        result = []  # To store the final MST.
        i = 0
        e = 0  # Variable to keep the count of edges and i.

        # Step 1:  Sort all the edges in non-decreasing order of their weight.
        # If we are not allowed to change the given graph, we can create a copy of graph.
        self.graph = sorted(self.graph,key = lambda item: item[2])
        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Iterate till number of edges in the graph not becomes equal to V-1 bcoz we know in MST there are V-1 edges.
        while e < self.V - 1:
            u,v,w = self.graph[i]
            i += 1
            x = self.find(parent,u)
            y = self.find(parent,v)

            # If including this edge does't cause cycle, include it in result
            # and increment the index of result for next edge.
            if x != y:
                result.append([u,v,w])
                self.union(parent,rank,x,y)
                e = e+1

        minimumTreeCost = 0
        print("Edges in constructed MST")
        for u,v,weight in result:
            minimumTreeCost += weight
            print("{} ----- {} == {}".format(u,v,weight))

        print("Minimum spanning Tree : {}".format(minimumTreeCost))


# Driver code
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.kruskalAlgo()




