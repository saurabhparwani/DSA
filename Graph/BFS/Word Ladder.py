# Problem Statement : https://leetcode.com/problems/word-ladder/
# Video Solution : https://www.youtube.com/watch?v=ZVJ3asMoZ18
# Follow Up Question : Word Ladder 2 .


# TC = O(26*N*N*W) First N for words in List , Second N for String Comparison and W For total no of words in the Queue at a given time. 26 is for a-z variations.
# SC = O(N+N+N) FOr Queue , visited set and wordlist set.
def ladderLength(beginWord,endWord,wordlist):
    visited = set()   # To store the all visited words as we can delete element from set during iteration in python.
    wordlist_set = set(wordlist)

    if endWord not in wordlist_set: # Base Case If the endWord is not present in the wordList simply return 0.
        return 0

    queue = [(beginWord,1)]  # Store the Word and Step Till we reached to that word in a Queue.

    while queue:
        word, step = queue.pop(0)

        # If word is equal to endWord then simply return the step.
        if word == endWord:
            return step

        if word in visited:  # If a word is already processed and is present in visited then simply continue ,Ignore that word.
            continue

        # Now traverse all the Variants of the Word and check which one is present in the wordlist.
        for i in range(len(word)):
            for j in range(0,26):   # Coz we have 26 character in the string.
                ord_val = ord('a') + j
                next_word = word[0:i] + chr(ord_val) + word[i+1:]     # Create the new Word from the Curr word .

                if next_word in wordlist_set:      # If next Word is Present in the String then Simply add that in Queue with step = curr_step+1
                    queue.append((next_word,step+1))
        visited.add(word)  # Mark this Word as the Visited Word.

    return  0    # If Word is not matched with any word then simply return 0 as it's not possible to covert words.


# Driver Code
beginWord = 'hit'
endWord = 'cog'
wordList = ['hot','dot','dog','lot','log','cog']
print(ladderLength(beginWord,endWord,wordList))
