# Problem Statement : https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/

# Utility Method to check that a particular node can be colored with col.
def isSafe(node,graph,color,col):

    for nbh in graph[node]:
        if color[nbh] == col:
            return False
    return True


# TC  = O(M^N) There are N Nodes and for each nodes we have M choices as the Color.
# SC  = O(N) + O(N) For Color Array and for recursion stack.
def solve(node,graph,color,n,m):

    # Base Case , If node is equal to total number of nodes in the graph then simply return True.
    if node == n:
        return True

    # Traverse for each color that a given node can be marked with Given Color.
    for i in range(1,m+1):
        # Check if it's safe to color this node with given node.
        if isSafe(node,graph,color,i):
            # If it's safe then call solve method for next node & if that node return true then return true else false.
            # Mark this node as the given color.
            color[node] = i
            if solve(node+1,graph,color,n,m):
                return True

            # Backtrack to revert all the changes to check all possible paths.
            color[node] = 0

    return False




# Driver Code
graph = [[0, 1, 1, 1 ],[ 1, 0, 1, 0 ],[ 1, 1, 0, 1 ],[ 1, 0, 1, 0 ]]
m = 3
v = 4
color = [0 for i in range(v)]

if solve(0,graph,color,v,m):
    print('Graph can be colored with M colors')
else:
    print('Graph can not be colored with M colors')

