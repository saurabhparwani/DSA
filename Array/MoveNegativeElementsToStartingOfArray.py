# This Method will Move All Positive  elements of Array to the start in-place .
# In this Algo order of positive numbers does not matter.

def movePositiveElementsToStart(arr):
    low = 0
    for i in range(len(arr)):
        if arr[i] >=0:
            arr[low],arr[i] = arr[i],arr[low]
            low+=1


# This Method will Move All negative elements of Array to the start in-place .
# In this Algo order of positive numbers does not matter.
def moveNegativeElementsToStart(arr):
    low = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[low] , arr[i] = arr[i], arr[low]
            low += 1

input = [-5, 7, -3, -4, 9, 10, -1, 11]
moveNegativeElementsToStart(input)
print(input)

input_two = [-5, 7, -3, -4, 9, 10, -1, 11]
movePositiveElementsToStart(input_two)
print(input_two)
