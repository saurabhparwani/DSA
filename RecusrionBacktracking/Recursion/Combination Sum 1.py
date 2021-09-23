# Problem Statement : https://www.youtube.com/watch?v=OyZFFqQtu98&list=PLgUwDviBIf0rQ6cnlaHRMuOp4H_D-7hwP
# Leetcode :  https://leetcode.com/problems/combination-sum/

def pickNonPick(ind,input,target,ds,ans):

    # If target becomes 0 then it means we have found the required sum and add it to the answer list & return.
    if ind == len(input):
        if target == 0:
           ans.append(list(ds))
        return

    # Optimization
    # if input[ind] > target:
    #     return

    # Pick the Element & Call same method  with same index & updated target ( Same index coz we can pick same element many times )
    if input[ind] <= target:
        ds.append(input[ind])
        pickNonPick(ind,input,target-input[ind],ds,ans)
        # Backtrack remove this element from the current list
        ds.pop()

    # Not Pick the Current Element & Move to next index with the same target.
    pickNonPick(ind+1,input,target,ds,ans)


# Method to generate All Possible Combination with given Sequence.
# TC = O(2^n)*K ( As there will be total 2^n sub sequence of the given list & assuming that K will be length of the sub sequence)
# SC = O(k*x) (Assuming that there will be total x combination total of length k each.)
def findCombination(input,target):
    ans = []
    ds = []
    pickNonPick(0,input,target,ds,ans)
    return ans

# Driver Code
input1 = [2]
answer = findCombination(input1,1)
print(answer)