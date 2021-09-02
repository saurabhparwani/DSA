# Method to Find the Next Permutation( in sorted Order)  of a given sequence . Steps :
# 1. Traverse the array from end and find pivot index such that a[i] > a[i+1]
# 2. Traverse the array from end and find index (break_point) of largest element lesser than pivot_index element.
# 3. Now swap the pivot_index and break_point index elements.
# 4. Now Reverse the array from pivot_index + 1 position to the end of array.


def reverse(arr,index):
    n = len(arr)-1

    for i in range(0,(n+1-index)//2):
        arr[index+i],arr[n-i] = arr[n-i],arr[index+i]

    return arr

def nexPermutationSequence(arr):
    n = len(arr)

    i = n-2

    # Find the Pivot Element
    while i >=0 and arr[i] > arr[i+1]:
        i-=1

    # If pivot_index  is not found then only reverse the whole array.
    if i >= 0:
        j = n-1

        # Find the first Element which is greater than the pivot index element
        while j >= 0 and arr[j] < arr[i]:
            j -= 1

        # Swap the pivot index element with the break_point index element.
        if j>=0:
            arr[i],arr[j] = arr[j],arr[i]

    # Reverse the array from the pivot_index +1 position
    return reverse(arr,i+1)


# Driver Code
input = [1,2,4,3]
print(nexPermutationSequence(input))