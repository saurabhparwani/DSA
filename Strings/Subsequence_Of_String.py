# Problem Statement :  https://www.geeksforgeeks.org/print-subsequences-string/

# Method 1 . Pick and don't pick concept.

def printSubsequence(input,output):

    if len(input) == 0:
        print(output)
        return

    # Include the First element of the input string to the output string.
    printSubsequence(input[1:],output+input[0])

    # Don't include the first element of the input string to the output .
    printSubsequence(input[1:],output)


input = 'abcd'
output = ''
printSubsequence(input,output)