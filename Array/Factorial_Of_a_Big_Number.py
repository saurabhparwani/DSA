def doNextMultiply(x,result,res_len):

    # Multiply given x value to every other element of result list starting from 0.
    i = 0
    carry = 0
    while i < res_len:

        # Get the Product of the List element , Store Unit Value to list and store Carry in another Iteration
        prod = result[i]*x + carry
        result[i] = prod % 10
        carry = prod//10
        i = i+1

    while carry :
        # Store Carry to the next place in result Array and Now result length will increase by 1
        result[res_len] = carry % 10
        carry = carry//10
        res_len = res_len+1

    return  res_len



def printFactorial(n):

    # Initialize the Result Array whose first element will be  1 as factorial of 0 & 1 is 1.

    result = [None]*1000
    result[0] = 1
    res_len = 1
    x=2
    while x <= n:
        # Multiply every digit one by one
        res_len = doNextMultiply(x,result,res_len)
        x+=1

    i=res_len-1

    while i >=0:
        print(result[i],end="")
        i-=1
    print()

# Call Print Factorial Method
printFactorial(5)
printFactorial(50)
printFactorial(100)
printFactorial(150)
printFactorial(200)
printFactorial(250)