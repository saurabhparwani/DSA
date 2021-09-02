def printPermutations(a,l,r):

    # Base Condition
    if l == r :
        print(''.join(a))  # To convert list into String
    else:
        # Swap  every character with first character one by one and call same permutations method for next l+1 size array.
        for i in range(l,r+1):

            a[i],a[l] = a[l],a[i]

            printPermutations(a,l+1,r)

            # Backtrack to revert previous change
            a[i],a[l] = a[l],a[i]

string = 'ABCD'
printPermutations(list(string),0,len(string)-1)