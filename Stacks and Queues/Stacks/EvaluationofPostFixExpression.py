# Method to Evaluate Postfix Expression.

def EvaluatePostFix(S):
    stack = []
    num1 = num2 = result = 0
    for ch in S:
        if ch == '*' or ch == '+' or ch == '-' or ch == '/':

            num2 = stack.pop()
            num1 = stack.pop()

            if ch == '*':
                stack.append(num1 * num2)
            elif ch == '-':
                stack.append(num1 - num2)
            elif ch == '+':
                stack.append(num1 + num2)

            elif ch == '/':
                stack.append(num1 // num2)
        else:
            stack.append(int(ch))

    return stack[0]


# Driver Method

post_fix = ['123+*8-','231*+9-','45+5*567-++']

for s in post_fix:
    print("Result of Postfix expression " + s +"  is {}".format(EvaluatePostFix(s)))