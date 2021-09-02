def partition(a,start,end):

    # Assign the Pivot Value & Index
     pivot = a[end]
     pivot_index = start
     for i in range(start,end,1):
         if a[i] <= pivot:
             a[i],a[pivot_index]= a[pivot_index],a[i]
             pivot_index += 1
     # Swap the Pivot_Index element with the last element so that Pivot element
     a[pivot_index],a[end] = a[end],a[pivot_index]
     return  pivot_index



def quickSort(arr,start,end):
    if start < end :

        # Find the Pivot Index
        pivot_index = partition(arr,start,end)

        # Call the Sort Algo to the left half of the Array
        quickSort(arr,start,pivot_index-1)

        # Call the Sort Algo to the right half of the Array
        quickSort(arr,pivot_index+1,end)

arr = [54,3,342,423,434,45,2342,1,5,43,32,422,33,22,11,60]

a = [4,6,3,2,1,5,6,7,8,9,3,4,5,9,8,7,6,1,4,3]
# quickSort(arr,0,len(arr)-1)
quickSort(a,0,len(a)-1)
print(arr)
print(a)