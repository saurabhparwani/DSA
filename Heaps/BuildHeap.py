# Problem Statement : https://www.geeksforgeeks.org/building-heap-from-array/

def heapifyMax(arr,i,n):
    # Let Suppose that element at current position is largest ,
    # now calculate it's left & right child and swap parent node with largest node.
    largest_index = i
    left_child = 2*i+1
    right_child = 2*i+2

    if left_child < n and arr[left_child] > arr[largest_index]:
        largest_index = left_child

    if right_child < n and arr[right_child] > arr[largest_index]:
        largest_index = right_child

    # If current element is not the larges among it's children
    # Swap the Current parent node with the largest Value and heapify
    if largest_index!=i:
        arr[i] , arr[largest_index] = arr[largest_index],arr[i]
        # Recursively heapify the affected sub-tree
        heapifyMax(arr,largest_index,n)

def buildMaxHeap(arr,n):
    # Get the index of first non leaf node as leaf nodes already fulfilling the condition of heap.
    start_index = n//2 - 1

    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node
    for i in range(start_index,-1,-1):
        heapifyMax(arr,i,n)


def heapifyMin(arr,i,n):
    # Let Suppose that element at current position is largest ,
    # now calculate it's left & right child and swap parent node with larget node.
    smallest_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] < arr[smallest_index]:
        smallest_index = left_child

    if right_child < n and arr[right_child] < arr[smallest_index]:
        smallest_index = right_child

    # If current element is not the larges among it's children
    # Swap the Current parent node with the largest Value and heapify
    if smallest_index != i:
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        # Recursively heapify the affected sub-tree
        heapifyMin(arr, smallest_index, n)

def buildMinHeap(arr,n):
    # Get the index of first non leaf node as leaf nodes already fulfilling the condition of heap.
    start_index = n // 2 - 1

    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node
    for i in range(start_index, -1, -1):
        heapifyMin(arr, i, n)

# Driver Code


# Driver Code
arr = [ 1, 3, 5, 4, 6, 13,10, 9, 8, 15, 17 ]
buildMaxHeap(arr,len(arr))
print("Array Representation of Max heap is :")
print(arr)

arr2 = [13, 3, 15, 1, 6, 4,8, 10, 9, 5, 17]
buildMinHeap(arr2,len(arr2))
print("Array Representation of Min heap is :")
print(arr2)