class Node(object):
    def __init__(self,val):
        self.val = val
        self.neighbour = []
# Problem Statement : https://leetcode.com/problems/clone-graph/
# TC = O(E+V)
def dfs(node,visited):
    # Base Case , IF node is None then simply return None
    if node is None:
        return None

    # Create the Copy Node and store it's reference / Actual Node into the map for future references.
    newNode = Node(node.val)
    visited[node.val] = newNode

    for nbh in node.neighbours:
        # If nbh is not visited/created then apply DFS for this newly found node.
        if nbh.val not in visited:
            dfs(nbh,visited)

        # If Node is already created and stored in the visited array then simply  append nbh node to current node neighbour.
        newNode.neighbour.append(visited[nbh.val])

    return newNode

def cloneGraph(node):
    visited  = {}
    return dfs(node,visited)


# Driver Code
adjList = [[2,4],[1,3],[2,4],[1,3]]