# All 8 Possible directions
global directions
directions = [[0,1],[0,-1],[-1,0],[1,0],[-1,1],[1,1],[1,-1],[-1,-1]]


# Method to Check if a Word exist in given 2D char Array in any direction or not.
def doesWordExistInAnyDirection(rd,cd,grid,word):

    # If the First character does not matches.
    if grid[rd][cd] != word[0]:
        return False


    # Get Row & Column size of grid.
    row_length = len(grid)
    column_length = len(grid[0])

    path = '('+str(rd)+','+str(cd)+')'

    # If first character matches then Search in All Possible Direction
    for x,y in directions:
        row = rd + x
        col = cd + y

        # Flag to detect that Word exist in current Iteration or not
        flag = True

        # Start Matching from second character
        for i in range(1,len(word)):

            # Check for boundary condition x,y exist in grid or not  & then match character
            if row >=0 and row <row_length and col >= 0 and col < column_length and grid[row][col] == word[i]:

                # This means word is matching with given character and now move forward in particular direction
                path +=  '('+str(row)+','+str(col)+')'
                row += x
                col += y

            # If any of above condition failed then flag will be false and break the current loop and then search in different direction
            else:
                flag = False
                # Reset to Default initial Path
                path = '(' + str(rd) + ',' + str(cd) + ')'
                break

        # If Word Matches in current direction then return true.
        if flag:
            print(path)
            # Reset to Default initial Path
            path = '(' + str(rd) + ',' + str(cd) + ')'
            return True

    return False # If Word does not matches in any given 8 direction then simply return the solution.


# Method to check Word. This method will traverse each element of the grid and then check that given word
# is starting from that word or not. If the first word matches then we will Check in All 8 Possible direction.
def searcIn2DArray(grid,word):
    if grid and word:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if doesWordExistInAnyDirection(i,j,grid,word):
                    print("Word Starting in row {} from column {} ".format(i,j))


grid = ["GEEKSFORGEEKS","GEEKSQUIZGEEK", "IDEQAPRACTICE"]
word = "EEE"

# Time Complexity of this Solution is O(R * C ) Given in GFG but  I think it would be something like ( R*C*K*8) Where K will be length of Word.
searcIn2DArray(grid,word)