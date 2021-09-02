# Problem Statement : https://leetcode.com/problems/3sum/

# Method 1 : Use three loops to find all possible triplets this will take O(N^3) time.
# Method 2 : Use Hash map to store the sum and use two loops to find all the triplets. TC = O(N^2) , SC = O(N)

# Method 3 : Optimized Method
# First Sort the list in ascending order and then fix i to the left side i.e 0.
# Now initialize j = i+1 and k = n-1 and this way find two number using two pointer technique who will give 0 after adding with nums[i].
def threeSum(nums):

    ans = []

    if nums is None or len(nums) < 3:
        return ans

    # Sort the input array
    nums.sort()
    n = len(nums)

    # Loop through complete array one by one.
    for i in range(0,n-2):

        # Check for duplicate triplet , if first item in triplet is already found then loop through next unique first element.
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j = i+1
        k = n-1

        while j < k:
            threeSum = nums[i] + nums[j] + nums[k]
            if threeSum < 0: # If sum is less than 0.
                j += 1
            elif threeSum > 0: # If sum is greater than 0.
                k -= 1
            else:
                ans.append([nums[i],nums[j],nums[k]])
                j += 1
                k -= 1
                # Optimization to avoid duplicates
                while j < k and nums[j] == nums[j-1]:j+=1
                while j < k and nums[k] == nums[k+1]: k-=1

    # Return the result array.
    return ans


# Driver Code

input1 = [-1,0,1,2,-1,-4]
input2 = []
input3 = [0]


print(threeSum(input1))
print(threeSum(input2))
print(threeSum(input3))

