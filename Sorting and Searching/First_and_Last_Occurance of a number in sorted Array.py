
# Iterative Method to get Location of 1st occurance of an element is sorted array.
def first_occurance(arr,ele):
    low = 0
    high = len(arr) - 1
    first_occ_index = -1
    while low <= high:

        mid = low + (high-low)//2

        if arr[mid] == ele:
            first_occ_index = mid
            high = mid -1

        elif arr[mid] < ele:
            low = mid+1

        else: high = mid-1

    return first_occ_index

def last_occurance(arr,ele):
    low = 0
    high = len(arr)-1
    last_occu_index = -1

    while low <= high :
        mid = low +(high-low)//2

        if a[mid] == ele:
            last_occu_index = mid
            low = mid+1

        elif a[mid] < ele :
            low = mid+1

        else :
            high = mid-1

    return last_occu_index


a = [1,1,2,2,3,4,5,5,5,5,6,6,7,8,8,10,12,12,14]

n = int(input("Enter a Number : "))
print("Fist occurrence  of {} is Index {} ".format(n,first_occurance(a,n)))
print("Last occurrence  of {} is Index {} ".format(n,last_occurance(a,n)))

if last_occurance(a,n) == -1 and first_occurance(a,n) == -1: count=0
else: count = last_occurance(a,n)-first_occurance(a,n)+1
print("Total Count of {} is {} ".format(n,count))