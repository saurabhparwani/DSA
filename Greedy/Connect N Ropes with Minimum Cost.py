# Problem Statement : https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/
import heapq

# Method 1 : Create a min heap and insert all the ropes in the min heap. Now add two smallest ropes from min heap first.
# Then add this new rope into the min heap and repeat this process until heap is not empty.
# Maintain a sum variable to store the cost of each operation.

# TC = O(N*LogN) As we are inserting n elements in the heap and each insertion & deletion takes LogN time.
# SC = O(N) For Heap Space.
def findMinimumCost(ropes):

    pq = []
    total_cost = 0
    # Insert all the ropes into the minheap.
    for rope in ropes:
       heapq.heappush(pq,rope)

    # Now apply the process on heap until heap is not empty.
    while len(pq) > 1:
        rope_1 = heapq.heappop(pq)
        rope_2 = heapq.heappop(pq)

        total_cost += (rope_1 + rope_2)
        heapq.heappush(pq,rope_1+rope_2)

    return total_cost


# Method 2 : Mathematical Approach
# Explaination : https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/
# TC = O(N*LogN)
# SC = O(1)


# Driver Code
ropes = [4,3,2,6]
print("Minimum cost to connect all the ropes {}".format(findMinimumCost(ropes)))
