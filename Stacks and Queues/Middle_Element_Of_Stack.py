# Problem Statement : https://www.geeksforgeeks.org/delete-middle-element-stack/
# Method to delete the middle element: 1. Go till bottom element of stack and keep a count to the current element.
# Then again add the current element into the stack only when the element is not middle element.

def deleteMiddleElement(stack,n,curr):
   # Base Case
    if  n == curr or n==0:
        return

    temp = stack.pop()
    deleteMiddleElement(stack,n,curr+1)

    if curr != (n//2):
        stack.append(temp)
    else:
        print("Middle Element : {}".format(temp))

# Driver Code
stack = [1,2,3,4,5,6,7]
deleteMiddleElement(stack,len(stack),0)

print("Stack After Removing the Middle Element")
print(stack)