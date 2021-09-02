# Problem Statement : Sort an arr using heap

# Helper Method for max heapify.
def  heapify(arr,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    # If current root is not the largest then Swap and heapify recursively.
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)


# Method to do heapSort . Steps : First we will build max heap using the array and then we will apply heapSort Algo.
# TC : O(N*LogN) As we are heapfying N-1 elements and heapify process takes O(logN) time.
def heapSort(arr):

    n = len(arr)
    # Build the max heap
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

    # Now Sort the array based on heap sort
    # Swap root ( max ) node everytime with the last node
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i] # Swap root value to last value.
        heapify(arr,i,0)


# Driver Code
arr = [1,5,14,12,6,2,9,8,17]
heapSort(arr)
print(arr)
