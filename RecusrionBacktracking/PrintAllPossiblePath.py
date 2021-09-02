# Problem Statement : https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/

# TC = O(2^N*M) , SC = O(N)
def findAllPathes(mat,x,y,path):

    if x == N-1 and y == M-1:
        path = path+str(mat[x][y])
        print(path)
        return

    if x >= N or y >= M:
        return

    findAllPathes(mat,x,y+1,path+str(mat[x][y]))
    findAllPathes(mat,x+1,y,path+str(mat[x][y]))


# Driver Code

N = 2
M = 2
mat = [[1,2],[3,4]]

findAllPathes(mat,0,0,'')