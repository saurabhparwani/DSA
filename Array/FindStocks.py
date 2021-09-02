def maxProfit(arr):
    min = 999999
    ma = arr[-1]
    min_index = len(arr)-1
    output = 0

    for i in range(len(arr)-2,-1,-1):
        if arr[i] > ma:

           if min_index > i:
              output = max(output,(ma - arr[min_index]))
           ma = min =  arr[i]
           min_index = i

        elif arr[i] < ma:
            if arr[i] < min:
                min = arr[i]
                min_index = i

    if ma - arr[min_index] > output:
        output = ma - arr[min_index]

    return output

arr = [7, 1, 5, 3, 6, 4]
print(maxProfit(arr))