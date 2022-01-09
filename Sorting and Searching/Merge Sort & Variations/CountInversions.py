# Problem Statement : https://www.geeksforgeeks.org/counting-inversions/

# Method 1: Brute force approach using nested loops to calculate inversions.
# TC = O(N*N) , SC = O(N)

# Method 2 : Using Merge sort method by  modifying the merge & mergeSortMethod.

def merge(arr,temp_arr,left,mid,right):

    i = left
    k = left
    j = mid+1
    inversion_count = 0

    # Traverse till we reach at boundary of any of the array.
    while i <= mid and j <= right:

        # Right element is Bigger or equal
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i+=1
            k+=1

        # Left element is bigger , now count inversions based upon the condition.
        # Add the mid+1 - i total number of element to the right side of the left bigger element including itself.
        else:
            inversion_count += (mid+1 - i)
            temp_arr[k] = arr[j]
            k+=1
            j+=1

    # If any element is remaining in left array then add it.
    while i <= mid:
        temp_arr[k] = arr[i]
        i+=1
        k+=1

    # If any element is remaining in right array then add it.
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1


    # Now copy temp array to it's original array.
    for i in range(left,right+1):
        arr[i] = temp_arr[i]

    # Return the Inversions count.
    return inversion_count



def mergeSort(arr,temp_arr,left,right):

    inversions = 0

    if left < right:
        mid = (left + right) // 2

        inversions += mergeSort(arr,temp_arr,left,mid)
        inversions += mergeSort(arr,temp_arr,mid+1,right)

        inversions += merge(arr,temp_arr,left,mid,right)

    return inversions

# Wrapper Method to count the inversion.
def countInversion(arr,n):

    # Create temporary array to store the actual array.
    temp_arr = [0]*n

    return mergeSort(arr,temp_arr,0,n-1)


# Driver code
arr = [33, 42, 9,9,8,4, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
print("Number of Inversions are {}".format(countInversion(arr,len(arr))))

