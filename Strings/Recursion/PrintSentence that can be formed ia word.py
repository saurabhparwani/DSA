# Problem Statement : https://www.geeksforgeeks.org/recursively-print-all-sentences-that-can-be-formed-from-list-of-word-lists/

def printSentence(arr):
    for word in arr:
        print(word,end = " ")
    print()


# TC = O(n^k) where n is the length of the input and k is the length of each input.
# SC = O(1)
def selectWord(input,index,n,picked_words):

    # Base Case , If index is equal to the n then simply print the Word list.
    if index == n:
        printSentence(picked_words)
        return

    word_set = input[index]

    for word in word_set:
        # Append the Current word in the picked words.
        picked_words.append(word)
        selectWord(input,index+1,n,picked_words)

        # Remove the picked word from the picked word list.
        picked_words.pop(-1)




def printAllSentences(input):
    picked_words = []
    selectWord(input,0,len(input),picked_words)



# Driver Code
input = [["You","we"],["have","are"],["sleep","eat","drink"]]
printAllSentences(input)