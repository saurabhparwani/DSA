# Problem Statement : https://leetcode.com/problems/greatest-sum-divisible-by-three/

def greatestSumDivisibleByThree(nums):

    rem = [0] * 3     # Create the array to store the reminder array.

    for num in nums:
        copy_rem = list(rem)
        for i in range(3):
            ind = (copy_rem[i] + num ) % 3
            rem[ind] = max(rem[ind],copy_rem[i] + num)

    return rem[0]




# Driver Code
nums = [1,2,3,4,4]
print("Greatest Sum divisible by 3 is {}".format(greatestSumDivisibleByThree(nums)))