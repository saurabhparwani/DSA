# Problem Link : https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/submissions/

# TC = O(D*Target*R)
# SC  = O(D*Target)
# Note : Execution of bottom up approach is faster than top down approach in leetcode.
def getNumberOfDiceRolls_DPBottomUo(r,dice,target):
    if target > r*dice : return 0  # Special Case , if it's not possible to get the target sum.
    if target == r*dice:return  1  # Special Case , if it's possible to get sum only once after getting max dice number on each throw.

    dp = [[0 for _ in range(target+1)]for _ in range(dice+1)]
    mod = int(10 ** 9 + 7)
    # If we have only 1 throw then we can have 1 chance of getting target sum equal to the range of the dice .
    for j in range(1,min(r+1,target+1)):
        dp[1][j] = 1

    for i in range(2,dice+1):
        for j in range(1,target+1):
            for k in range(1,min(j,r+1)):
                    dp[i][j] += dp[i-1][j-k]
            dp[i][j] %= mod      # Step for Leetcode Question

    return dp[dice_rolls][target]




# TC = O(D*R)
# SC = O(d*t) For Storing the Sum
def helper(t,d,r,memo):

    if t == 0 and d == 0:      # Base case, If target is achieved in given dice rolls.
        return 1
    if t <= 0 or d <= 0:         # If Dice rolls are 0 & target is not achieved or target is negative.
        return 0
    # Check if the sub problem has been already solved or not.
    if (d, t) in memo:
        return memo[(d,t)]
    i = 1
    count = 0
    while i <= r:
        count += helper(t-i,d-1,r,memo)
        i+=1

    memo[(d, t)] = count  # Storing the result for memoization purpose.
    return count

def getNumberOfDiceRolls(target,dice_rolls,r):
    memo = {}
    answer = helper(target,dice_rolls,r,memo)
    return answer % (10 ** 9 + 7)




# Driver Code
dice_rolls = 3
r = 6
target = 8

print("Number of Dice Rolls is {}".format(getNumberOfDiceRolls(target,dice_rolls,r)))
print("Number of Dice Rolls is {}".format(getNumberOfDiceRolls_DPBottomUo(r,dice_rolls,target)))