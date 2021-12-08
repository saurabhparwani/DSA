# Problem Statement :

# TC = O(T*N) Where T is the target and N is the length of the nums array.
# SC = O(N) 
def getCombinations_DP(nums,target):

    dp = [0] * (target + 1)
    dp[0] = 1

    for i in range(target+1):

        for num in nums:
            if i - num >= 0:
                dp[i] = dp[i] + dp[i-num]

    return dp[target]


# Recursive Method
def helperMethod(nums,target,curr_arr,answer):
    if target == 0:                   # Base case when Sum is matched.
        answer.append(list(curr_arr))
        return
    if target < 0:return        # If Target becomes negative than simply return .
    for num in nums:
        curr_arr.append(num)
        helperMethod(nums,target-num,curr_arr,answer)
        curr_arr.pop()

def getCombinations(nums,target):
    answer = []
    curr_arr = []
    helperMethod(nums,target,curr_arr,answer)
    return answer


# Driver Code
nums = [1,2,3]
target = 3

# answer = getCombinations(nums,target)
#
# for ans in answer:
#     print(ans)

print("Total number of combinations are {}".format(getCombinations_DP(nums,target)))