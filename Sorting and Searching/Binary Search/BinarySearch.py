
# Iterative Method to perform Binary Search
def binarySearchIterative(a,ele):
    low = 0
    high = len(a)-1
    while low <= high:
        # Get the middle index
        mid =  low + (high-low)//2
        if a[mid] == ele:
            print("Element {} Found at Position {} ".format(ele,mid))
            return
        elif a[mid] < ele:
            low = mid+1
        else:
            high = mid-1
    print("Element {} Not found in Array".format(ele))

# Recursive Method to Perform Binary Search in a Sorted Array

def binarySearchRecursive(a,elment,low,high):

    if low <= high:
        mid = low + (high-low)//2

        if a[mid] == elment:
           print("Element {} Found at Position {}".format(elment,mid))

        # Search in the Right Half of the Array
        elif a[mid] < elment :
             binarySearchRecursive(a,elment,mid+1,high)

        # Search in the Left Half of the Array
        else:
            binarySearchRecursive(a,elment,low,mid-1)

    else:
        print("Element {} not found in Array".format(elment))

a = [1,2,4,5,8,13,15,16,19,32,36,45,55,61,78,89,95,110,115,127,145]
binarySearchIterative(a,115)
binarySearchRecursive(a,115,0,len(a)-1)