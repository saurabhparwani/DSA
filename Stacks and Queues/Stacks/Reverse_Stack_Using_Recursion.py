# https://www.geeksforgeeks.org/reverse-a-stack-using-recursion/

# Method to insert the element at the bottom of the stack.
def insertAtBottom(stack,item):

    if len(stack) == 0:
        stack.append(item)
        return

    curr = stack.pop()
    insertAtBottom(stack,item)
    stack.append(curr)



# Method to Reverse the stack Using Recursion. Steps will be
# 1. Pop the top element of the stack and store in the variable.
# 2. Now get the reverse of array other than popped element.
# 3. Now again append that popped element to the bottom of the reversed array.

# TC = O(N*N) , SC = O(1)  TC is N*N as we are Popping every element and then again inserting into the Bottom so that will take O(N*N) space.
def reverseStack(stack):

    if len(stack) < 1:
        return
    item = stack.pop()
    reverseStack(stack)
    insertAtBottom(stack,item)
    return stack

# Driver Code

stack = [4,1]
print(reverseStack(stack))
