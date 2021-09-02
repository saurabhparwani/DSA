def bubbleSort(arr):
    n=len(arr)
    for i in range(0,n):
        swapped=False   # Boolean Flag to improve efficiency in case Array is already Sorted
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if swapped is False:
            break


def selectionSort(a):
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if a[min_index]>a[j]:
                min_index=j
        a[i],a[min_index]=a[min_index],a[i]


def insertionSort(a):
    n=len(a)
    for i in range(1,n):
        ele = a[i]
        j=i-1
        while j > -1 and a[j]>ele:
            a[j+1]=a[j]
            j-=1
        a[j+1]=ele



a=[9,4,5,1,6,5,4,5,6,9,2,5]
b=[4,6,1,9,14,16,12,18,19,21,24]
bubbleSort(a)
print(a)
bubbleSort(b)
print(b)
selectionSort(a)
print(a)
selectionSort(b)
print(b)
insertionSort(a)
print(a)
insertionSort(b)
print(b)


