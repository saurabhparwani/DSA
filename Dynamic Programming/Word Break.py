# Problem Statement : https://leetcode.com/problems/word-break/


# TC = O(N*N)* D ( N^2 for two for loops and D for comparing the sub string in the dictionary.
# SC = O(N)
def wordBreak_DPTabulation(s,word_dict):

    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    # Now loop through complete string and solve smaller sub problem.
    for i in range(1,n+1):
        for j in range(i-1,-1,-1):

            # If Smaller Sub Problems are solved then current Substring is present in dictionary.
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True

    return dp[n]


def helper(s,wordDict,m):

    # Base Case
    if len(s) == 0:return True


    # Memoization Step , If the problem s already solved then return the precomputed result.
    if s in m:return m[s]


    for word in wordDict:
        if s[0:len(word)] == word and helper(s[len(word):],wordDict,m):
            m[s] = True
            return True

    # If Current String is not in the dictionary with any prefix.
    m[s] = False
    return False


# Solution using Memoization technique.
def wordBreak_Memoization(s,word_dict):
    m = {}
    return helper(s,word_dict,m)



# TC = O(2^n)
def wordBreak(s,dictionary):
    if len(s) == 0:
        return True

    for word in dictionary:
        # If the prefix is available in the dictionary and recursive method also returned true.
        if s[0:len(word)] == word and wordBreak(s[len(word):],dictionary):
            return True

    return False

# Driver Code

s = 'leetcode'
word_dict = ('leet','code')
print(wordBreak(s,word_dict))
print(wordBreak_DPTabulation(s,word_dict))
print(wordBreak_Memoization(s,word_dict))