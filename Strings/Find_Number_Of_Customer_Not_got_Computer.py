def findNo(n,str):
    ans = 0
    a =[0]*26
    total = n

    for i in str:
        index = ord(i) - ord('A')

        if a[index] == 0 and total > 0:
            a[index] = 1
            total -=1

        elif a[index] == 0 and total < 1:
            a[index] = -1
            ans +=1

        elif a[index] == 1:
            a[index] = 0
            total+=1

        elif a[index] == -1:
            a[index] = 0

    return ans



# Driver Code
str = 'ABCBCADEED'
print(findNo(1,str))