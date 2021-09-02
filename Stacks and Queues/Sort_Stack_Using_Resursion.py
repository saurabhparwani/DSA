# https://www.geeksforgeeks.org/sort-a-stack-using-recursion/

# Method to insert any element into the sorted stack .
# If the stack is empty or new element is largest element into the stack then simply append it otherwise
# insert the item into the correct place.
def sortedInsert(stack,item):

    # Base Case
    if len(stack) == 0 or stack[-1] <= item:
        stack.append(item)
        return

    curr = stack.pop()
    sortedInsert(stack,item)
    stack.append(curr)

# Method to sort the stack using recursion. Steps
# 1. Pop the top element of the stack and store this in another variable.
# 2. Now sort the remaining stack.
# 3. Now again insert the Popped element into the correctPosition using the sortedInsert Method.

# TC = O(N*N) , SC = O(1)  TC is N*N as we are Popping every element and then again inserting into the sorted order so in worst case it will take approx O(N*N) time.
def sortStack(stack):

    # Base Case
    if  len(stack) < 1:
        return stack

    item = stack.pop()
    sortStack(stack)
    sortedInsert(stack,item)

    return stack

# Driver Code
stack = [6203 ,4626 ,5470, 2039, 5917 ,3406, 5534, 7005, 2470, 9854 ,4993, 362, 9820, 3295, 7196 ,4037, 9405 ,8768 ,5405 ,1712 ,3215 ,3101 ,3752, 2140 ,5438 ,4994 ,1760, 9573 ,6271, 3790 ,9624 ,2473 ,9494 ,6171 ,5590 ,5409, 9577, 2201 ,2412 ,3124 ,2053 ,8483 ,3485 ,2950 ,2856 ,1759, 6986, 3338, 525, 3469, 5049, 4819 ,6569 ,8801, 6958 ,3084 ,4872, 8717, 3734 ,1141, 2505, 3357, 3613, 3077, 605, 280, 8485 ,1259, 2480, 1975, 5462, 5611, 456 ,8946, 8561 ,4390, 1782, 6624 ,7728, 3386 ,1170, 2775 ,8204, 7738]

print(sortStack(stack))