def pattern_1(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end='')
        print()
    print('__________________________________________')

def pattern_2(n):
    for i in range(n):
        for j in range(n):
            if j <= n-i-1:
                print('*',end='')
        print()
    print('__________________________________________')

def pattern_3(n):
    for i in range(n):
        for j in range(n):
            if j >= n-i-1:
                print('*',end='')
            else:
                print(' ',end='')
        print()
    print('__________________________________________')

def pattern_4(n):
    for i in range(n):
        for j in range(n):
            if j >= i:
                print('*',end='')
            else:
                print(' ',end='')
        print()
    print('__________________________________________')

def pattern_5(n):
    for i in range(n):
        for j in range(2*n-1):
            if j >= n-1-i and j <= n-1+i:
                print('*',end='')
            else:
                print(' ',end='')
        print()
    print('__________________________________________')

def pattern_6(n):
    for i in range(n):
        k =1
        for j in range(2*n-1):
            if j >= n-1-i and j <= n-1+i and k == 1:
                print('*',end='')
                k=0
            else:
                print(' ',end='')
                k=1
        print()
    print('__________________________________________')

def pattern_7(n):
    if n%2==0:
        x = (n-1)//2
    else:
        x = n //2
    k = -1
    for i in range(n):
        if i <= x:
            k += 1
        else:
            if n % 2 ==0 and i == x+1: k+=1
            k-=1
        for j in range(n):
           if j >= x-k and  j <= x+k:
               print('*',end=' ')
           else:
               print(' ',end=' ')
        print('')
    print('__________________________________________')



n = int(input('Enter the Number of lines : '))
# pattern_1(n)
# pattern_2(n)
# pattern_3(n)
# pattern_4(n)
# pattern_5(n)
# pattern_6(n)
pattern_7(n)
