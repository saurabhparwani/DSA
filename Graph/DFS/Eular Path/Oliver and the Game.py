# Problem Statement : https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/practice-problems/algorithm/oliver-and-the-game-3/
# Video Solution : https://www.youtube.com/watch?v=5h1JYjin_4o

# TC = O(V+E) We are doing Simple DFS for the Graph.
# SC = O(V+V) To store the In time & Out time in the Array.

global timer
timer = 1

def dfs(node,parent,graph):
    global timer
    intime[node] = timer
    timer += 1

    for nbh in graph[node]:
        if nbh!=parent:
            dfs(nbh,node,graph)

    outtime[node] = timer
    timer +=1



# Method to check that two nodes are subtree of each other or not.
def check(x,y):
    if intime[x] > intime[y] and outtime[x] < outtime[y]:
        return True
    return False


# Driver Code
n = int(input())
graph = [[] for i in range(n+1)]
for i in range(1,n):
    x,y = map(int,input().split())
    graph[x].append(y)

intime = [0]*(n+1)
outtime = [0]*(n+1)

dfs(1,0,graph)


q = int(input())

for _ in range(q):
    d,x,y = map(int,input().split())

    # If both nodes are not Subtree of each other then there is no way to reach Bob to Oliver
    if check(x,y) == False and check(y,x)== False:
        print("No")
        continue

    #  Now Check for Up Direction when Bob is moving in Up Direction
    if d == 0:
        # If Bob is in Subtree of Oliver Subtree , i.e y is coming below to X. and bob is moving in Up diection.
        if check(y,x):print("Yes")
        else:print("No")

    # If Bob can Move in DOwn direction only.
    elif d == 1:
        # If Oliver is below to Bob and Subtree , i.e X is coming below to u and Bob is moving in Down direction.
        if check(x,y):print("Yes")
        else:print("No")