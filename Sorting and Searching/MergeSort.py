def merge(a,left,middle,right):
    # Get the Left Array
    left_array = a[left:middle+1]
    right_array = a[middle+1:right+1]

    # Initial values for variables that we use to keep
    # track of where we are in each array

    left_index=0
    right_index=0
    sorted_indes = left

    # Go through both copies until we run out of elements in one

    while left_index < len(left_array) and right_index < len(right_array):
        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)

        if left_array[left_index] <= right_array[right_index]:
            a[sorted_indes] = left_array[left_index]
            left_index+=1
        else:
            a[sorted_indes]=right_array[right_index]
            right_index+=1
        sorted_indes+=1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them

    while left_index < len(left_array):
        a[sorted_indes]=left_array[left_index]
        left_index+=1
        sorted_indes+=1

    while right_index < len(right_array):
        a[sorted_indes]= right_array[right_index]
        right_index+=1
        sorted_indes+=1





def merge_sort(a,left,right):
    if left < right:
        # middle = (left+(right-1))//2     #  It is Same as (left + right ) //2
        middle = left + (right - left)//2
        merge_sort(a,left,middle)
        merge_sort(a,middle+1,right)
        merge(a,left,middle,right)


a=[33, 42, 9,9,8,4, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
print(a)
merge_sort(a,0,len(a)-1)
print(a)

# Time Complexity :  O(NLogN)

# Auxiliary Space Complexity :  O(N)