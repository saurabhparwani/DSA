# Method to Print Common Elements in three Sorted Array.
# We will be using 3 pointer technique to identify the common elements.


def printCommonElementin3SortedArray(a,b,c):
    i=j=k=0
    len_a = len(a)
    len_b = len(b)
    len_c = len(c)
    while i <len_a and j < len_b and k < len_c :

        # If all three elements are same .
        if a[i] == b[j] and c[k] == b[j]:
            print(a[i], end= " ")
            i+=1
            j+=1
            k++1

        # A[i] is less than B[j]
        elif a[i]< b[j]:
            i+=1

        # B[j] is less than C[k]
        elif b[j]<c[k]:
            j+=1

        # C[k] is the Smallest Element
        else :
            k+=1


arr1= [1, 5, 5]
arr2= [3, 4, 5, 5, 10]
arr3= [5, 5, 10, 20]

printCommonElementin3SortedArray(arr1,arr2,arr3)