# Problem Statement :  https://practice.geeksforgeeks.org/problems/subset-sums2234/1#
# Video Solution = https://www.youtube.com/watch?v=rYkfBRtMJr8&list=PLgUwDviBIf0rQ6cnlaHRMuOp4H_D-7hwP&index=4

def recursive(arr,index,sum,answer):

    if index == len(arr):
        answer.append(sum)
        return

    # Not Include Current index element in Sum
    recursive(arr,index+1,sum,answer)

    # Include Current index element in the Sum.
    recursive(arr,index+1,sum+arr[index],answer)

# TC = O(2^n) For generating the all possible subsets + O(2^n log 2^n) For Sorting the output.
# SC = O(2^n) For storing the  all possible sums in the answer list. And for recursions stack.
def subsetSum(arr):

    # Create an empty array to store the Sums.
    answer = []
    sum = 0
    recursive(arr,0,sum,answer)   # Call the recursive method from 0th index.

    # Sort the answer array and return that
    answer.sort()
    return  answer


# Driver Code

arr = [3,1,2]

answer = subsetSum(arr)
print(answer)
