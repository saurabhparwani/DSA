# Problem Statement : https://leetcode.com/problems/clone-graph/submissions/
from collections import deque
class Node(object):
    def __init__(self,val):
        self.val = val
        self.neighbor = []

# TC = O(V+E) Simple BFS
# SC = O(V+V+V) For Queue & Map & Visited Array.
def cloneGraph(node):
    if node is None:     # Base case , IF the Node is Null then return Null.
        return node

    # Create a map to store the Newly created Nodes and Visited set to store visited nodes.
    mapper = {}
    mapper[node] = Node(node.val)
    vi = set()

    queue = deque()
    queue.append(node)
    while queue:
        # Process the Curr node  & add it to visited set as this node is visited.
        curr  = queue.popleft()
        vi.add(curr)

        # Process all the neighbour nodes & Created Unvisited nodes & add edges for nodes.
        for nbh in curr.neighbor:
            # If neighbor is not visited  yet.
            if nbh not in vi:
                if mapper.get(nbh) == None:
                    mapper[nbh] = Node(nbh.val)

                # Add the edges to the clone graph
                mapper[curr].neighbor.append(mapper[nbh])
                mapper[nbh].neighbor.append(mapper[curr])

            # Add neighbor to the Queue.
            queue.append(nbh)

    # Return Copy of the Starting node
    return mapper[node]

# Driver Code
adjList = [[2,4],[1,3],[2,4],[1,3]]