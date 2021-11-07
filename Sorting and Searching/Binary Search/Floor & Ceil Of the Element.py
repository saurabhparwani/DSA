# Problem Statement : https://www.geeksforgeeks.org/floor-in-a-sorted-array/

def findCeil(arr,num):

    low = 0
    high = len(arr) - 1

    ceil = -1

    while low <= high:
        mid = low + (high - low)//2

        if arr[mid] == num:
            return arr[mid]

        elif arr[mid] > num:
            ceil = arr[mid]
            high = mid - 1

        else:
            low = mid + 1

    return ceil


def findFloor(arr,num):

    low = 0
    high = len(arr) - 1

    floor = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == num:
            return arr[mid]

        elif arr[mid] < num:
            floor = arr[mid]
            low = mid + 1

        # This means this element is the smaller than the num so it is floor now find larger number lesser than num.
        else:
             high = mid - 1

    return floor


# Driver Code
arr = [1, 2, 8, 10, 10, 12, 19]
num = 3

print("Floor of the given number is {}".format(findFloor(arr,num)))
print("Ceil of the given number is {}".format(findCeil(arr,num)))