# Problem Statement : Dijkstra's Algorithm
import heapq


def dijkstraAlgo(graph,starting_vertex):
    distances = {vertex:float('infinity') for vertex in graph}

    # Mark the distance from source to itself as 0. And add this to Priority Queue.
    distances[starting_vertex] = 0
    pq = [(starting_vertex,0)]  

    while len(pq) !=0:

        current_vertex, current_distance = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (neighbor,distance))

    return distances


# Time Complexity: The time complexity of the above code/algorithm looks O(V^2) as there are two nested while loops.
# If we take a closer look, we can observe that the statements in inner loop are executed O(V+E) times (similar to BFS).
# The inner loop has decreaseKey() operation which takes O(LogV) time. So overall time complexity is O(E+V)*O(LogV) which is O((E+V)*LogV) = O(ELogV)
# Note that the above code uses Binary Heap for Priority Queue implementation. Time complexity can be reduced to O(E + VLogV) using Fibonacci Heap.
# The reason is, Fibonacci Heap takes O(1) time for decrease-key operation while Binary Heap takes O(Logn) time.

# Space Complexity : O(V) for Priority Queues


# Driver Code

example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

print("Shortest path from Source vertex to all other vertices")
print(dijkstraAlgo(example_graph,'X'))
