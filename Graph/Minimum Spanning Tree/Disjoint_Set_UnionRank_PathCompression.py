# Problem Statement : https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/

# A union by rank and path compression based
# program to detect cycle in a graph
from collections import defaultdict

class Graph(object):

    def __init__(self,vertex):
        self.vertex = vertex
        self.edges = defaultdict(list)

    def addEdge(self,u,v):
        self.edges[u].append(v)

class Subset(object):

    def __init__(self,parent,rank):
        self.parent = parent
        self.rank = rank

# A utility function to find set of an element node(uses path compression technique)
def find(subsets,node):

    # If node is not the root node then find the parent of the node and update the parent of the node.
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets,subsets[node].parent)

    return subsets[node].parent

# A function that does union of two sets of u and v(uses union by rank)
def union(subsets,u,v):

    # Attach smaller rank tree under root of high rank tree(Union by Rank).
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u

    elif subsets[u].rank < subsets[v].rank:
        subsets[u].parent = v

    # If ranks are same, then make one as root and increment its rank by one.
    else:
        subsets[v].parent = u
        subsets[u].rank += 1

# The time complexity of both operation find & union becomes even smaller than O(Logn).
# In fact, amortized time complexity effectively becomes small constant.

def isCycle(graph):

    # Make Subsets from the given graph.
    subsets = []
    for u in range(graph.vertex):
        subsets.append(Subset(u,0))

    # Iterate through all edges of graph, find sets of both vertices of every
    # edge, if sets are same, then there is cycle in graph.
    for u in graph.edges:
        u_parent = find(subsets,u)
        for v in graph.edges[u]:
            v_parent = find(subsets,v)

            # If both nodes are in same set then this means cycle exist.
            if u_parent == v_parent:
                return True

            # Else combine both the nodes in the same set.
            else:
                union(subsets,u_parent,v_parent)

    # If everything goes fine this means cycle does not exist.
    return False


# Driver Code
g = Graph(4)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(0,3)
g.addEdge(0,2)

if isCycle(g):
    print("Graph Contains Cycle")
else:
    print("Graph does not contain Cycle")