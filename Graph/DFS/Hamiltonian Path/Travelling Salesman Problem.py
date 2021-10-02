# Problem  Link : https://www.geeksforgeeks.org/travelling-salesman-problem-implementation-using-backtracking/?ref=rp

# TC = O(N!)  , For N nodes time complexity = N * (N – 1) * . . . 1 = O(N!)
# SC =  O(N)  ,
def travelling_salesman_problem(graph,visited,node,total_vertices,count,cost,answer):

    # Base Case , If count becomes the total number of vertices and there exist a path between last node to starting node
    # and cost of that path is less tha is less than existing cost then update maximum cost.
    if count == total_vertices and graph[node][0] != 0 and (cost + graph[node][0] < answer[0]):
        answer[0] = cost + graph[node][0]
        return

    # Now Traverse through each path and explore each unvisited vertex one by one.
    for i in range(total_vertices):
        if visited[i] == False and graph[node][i] != 0:

            # Mark node as visited
            visited[i] = True
            travelling_salesman_problem(graph,visited,i,total_vertices,count+1,cost+graph[node][i],answer)

            # Mark node as Unvisited , Backtrack to find all possible paths
            visited[i] = False




# Driver Code
n = 4
graph= [[ 0, 10, 15, 20 ],
            [ 10, 0, 35, 25 ],
            [ 15, 35, 0, 30 ],
            [ 20, 25, 30, 0 ]]

visited = [False for i in range(n)]
# Mark 0th node as visited
visited[0] = True
answer = [1000000]
# Find the minimum weight Hamiltonian Cycle
travelling_salesman_problem(graph, visited, 0, n, 1, 0,answer)

print("Minimum Cost to cover all the cities {}".format(answer[0]))