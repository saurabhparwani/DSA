# Given an array, print the Next Greater Element (NGE) for every element.
# The Next greater Element for an element x is the first greater element on the right side of x in the array.
# Elements for which no greater element exist, consider the next greater element as -1.

# Example 1: Input = [4, 5, 2, 25]  , Output = [5,25,25,-1]
# Example 2: Input = [13, 7, 6, 12]  , Output = [-1,12,12,-1]


# Brute force Approach of finding NGE for each element . TC = O(N*N) , SC = O(1).
def NGE_BruteForce(arr):
    n = len(arr)
    # nge_array = [-1]*n

    for i in range(0,n-1):
        flag = 0
        for j in range(i+1,n):
            if arr[i] < arr[j]:
                # nge_array[i] = arr[j]
                flag = 1
                print(str(arr[i])+' --> ' + str(arr[j]))
                break
        if flag == 0:
            print(str(arr[i]) + ' --> ' + str(-1))
    print(str(arr[n-1])+' --> ' + str(-1),end='\n----------------------\n')

# Optimized Approach using stack to find NGE for each array. TC = O(N) , SC = O(N)
# But this code is not preserving the order of output in the order of input. As 21 is before 3 in input but in output it is after 3.
# To maintain the order of the output we will process array from right to left instead of left to right.
def NGE_Stack(arr):
    n = len(arr)
    nge_array = [-1] * n
    stack = []
    stack.append(arr[0])
    # Traverse the complete array.
    for i in range(1,n):

        while len(stack)>0 and stack[-1] < arr[i]:
            ele = stack.pop()
            print(str(ele) + ' --> ' + str(arr[i]))

        stack.append(arr[i])

    while stack:
        print(str(stack.pop())+ ' --> ' + str(-1))
    print('--------------')


# Optimized Solution with Stack. TC = O(N), SC = O(N) . In this Solution we will process the array from right to left to maintain the order.
def NGE_Stack_OrderMaintain(arr):
    n = len(arr)
    stack = []
    nge_arr = [-1] * n

    # Traverse array from right to left to maintain the order
    for i in range(n-1,-1,-1):

        # Keep Popping the element from the stack till top element of stack is less than curr array element
        while len(stack) > 0 and stack[-1] < arr[i]:
            stack.pop()

        # If stack is not empty after popping then it means top of the stack is the next greater element for that array element.
        if stack:
            nge_arr[i] = stack[-1]

        # Else no greater element is present in right side.
        else:
            nge_arr[i] = -1

        # Add the current element into the stack.
        stack.append(arr[i])

    # Print the Complete output array.
    for i in range(0,n):
        print(str(arr[i])+ ' --> ' + str(nge_arr[i]))

# Driver Code
input_arr = [6,8,0,1,3]
NGE_BruteForce(input_arr)
NGE_Stack(input_arr)
NGE_Stack_OrderMaintain(input_arr)

# Another Similar Problem : Next Smaller Element
# https://www.geeksforgeeks.org/next-smaller-element/

