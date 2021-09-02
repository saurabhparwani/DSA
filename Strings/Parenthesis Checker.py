# Problem Statement : https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1

# Method to Check that Parenthesis sequence is Valid or not.
# TC = O(N) , SC = O(N) For Stack.
def ispar(x):
    stack = []
    count = 0
    for i in x:
        # If element is opening bracket than append into stack.
        if i == '{' or i == '[' or i == '(':
            stack.append(i)
            count += 1

        # If element is closing bracket than check that stack is not empty and top element is the opening bracket of same type.
        elif i == '}' or i == ']' or i == ')':
            if i == '}':
                if count < 1 or stack[-1] != '{':
                    return False
                else:
                    stack.pop()
                    count -= 1
            elif i == ']':
                if count < 1 or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
                    count -= 1

            elif i == ')':
                if count < 1 or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
                    count -= 1

    if len(stack) > 0:
        return False

    return True


# Driver Code

str = '([]'

if ispar(str): print("Parenthesis expression is Balanced.")
else:print("Parenthesis expression is not Balanced.")