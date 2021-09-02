# Problem Statement : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def findMaxProfit(arr,n):

    curr = arr[n-1]
    maximum = arr[n-1]
    max_profit = 0

    for i in range(n-2,-1,-1):

        if arr[i] < maximum:

            if max_profit < (maximum - arr[i]):
                max_profit = maximum - arr[i]

        elif arr[i] > maximum:
            maximum = arr[i]

    return max_profit

# Driver Code

prices = [7,1,5,3,6,4]
print("Maximum Profit by selling shares {}".format(findMaxProfit(prices,len(prices))))
