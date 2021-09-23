# Problem Statement :  https://leetcode.com/problems/subsets-ii/
# Video Solution : https://leetcode.com/problems/subsets-ii/


def recursive(arr,index,ds,answer):

    # Add Current Size Valid Subset in the final List.
    answer.append(list(ds))

    # Go through All the Possible element to find Subset of bigger size  than current size.
    for i in range(index,len(arr)):

        if i > index and arr[i] == arr[i-1]: # To avoid duplicates subsets.
            continue

        ds.append(arr[i]) # Add Current item in the list.
        recursive(arr,i+1,ds,answer)  # Call the recursive method from the next index.
        ds.pop()  # Backtrack to revert the added item


# TC = O(2^n^K) where K is the Length of the Each Subsets.
# SC = O(K*X) Where K is the size of each subset and X is the total number of unique subsets.
def generateAllSubsets(arr):

    answer = [] # Initialize and empty answer & ds list.
    ds = []
    arr.sort()  # If In case Given output is not in sorted order because duplicates are not allowed .
    recursive(arr,0,ds,answer)      # Call the recursive method from the 0th index starting subset of size 1.
    return answer

# Driver Code
arr = [4,4,4,1,4]
answer = generateAllSubsets(arr)
print(answer)