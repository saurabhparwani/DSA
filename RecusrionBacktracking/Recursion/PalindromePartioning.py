# Problem Statement :   https://leetcode.com/problems/palindrome-partitioning/
# Video Solution : https://www.youtube.com/watch?v=WBgsABoClE0&t=1103s

# Helper Method to check palindrome.
def isPalindrome(str,start,end):
    while start <= end:
        if str[start] != str[end] : return False
        start += 1
        end -= 1
    return True

def partition(str,index,ans,path):

    # Base Case (If index is equal to length of the string then simply add them into answer)
    if index == len(str):
        ans.append(list(path))
        return

    # Find all the Possible Points where we can mark Cuts.
    for i in range(index,len(str)):

        # If it is palindrome then Only we will mark cuts
        # Call for same recursive method from the next index
        # Call the same method from index + 1 position.
        if isPalindrome(str,index,i):
            path.append(str[index:i+1])
            partition(str,i+1,ans,path)
            path.pop()



def findPalindromePartioning(str):
    ans = []
    path = []
    partition(str,0,ans,path)
    return ans




# Driver Code

s = "aabb"

answer = findPalindromePartioning(s)

print(answer)





