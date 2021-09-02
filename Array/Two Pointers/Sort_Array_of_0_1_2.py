def sortArray_Of_0_1_2(a):
    low=0
    mid=0
    high = len(a) - 1
    while mid<=high :
        if a[mid]==1:
            mid+=1
        elif a[mid]==0:
            a[low],a[mid] = a[mid],a[low]
            low+=1
            mid+=1
        elif a[mid]==2:
            a[mid],a[high]=a[high],a[mid]
            high-=1


a= [1,1,1,1,2,1,0,1,2,2,0,2,2,1,1]
sortArray_Of_0_1_2(a)
print(a)