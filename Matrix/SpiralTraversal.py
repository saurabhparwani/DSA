# Direction Variable Meaning
# 1 = Left to right
# 2 = Top to Bottom
# 3 = Right ro left
# 4 = Bottom to Top

def SpiralOrderTraversal(a,n,m):
    left=top=0
    right=m-1
    bottom=n-1
    direction=1
    while top<=bottom and left<=right:
        if direction==1:
            for i in range(left,right+1):
                print(a[top][i],end=" ")
            top+=1
        elif direction==2:
            for i in range(top,bottom+1):
                print(a[i][right],end=" ")
            right-=1
        elif direction==3:
            for i in range(right,left-1,-1):
                print(a[bottom][i],end=" ")
            bottom-=1
        elif direction==0:
            for i in range(bottom,top-1,-1):
                print(a[i][left],end=" ")
            left+=1
        direction=(direction+1)%4

a=[[1,2],[5,6],[9,10]]
SpiralOrderTraversal(a,3,2)