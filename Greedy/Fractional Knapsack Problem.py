# Problem Statement: https://www.geeksforgeeks.org/fractional-knapsack-problem/

class Item(object):
    def __init__(self,weight,value):
        self.weight = weight
        self.value = value

# TC = O(NLOGN) For Sorting
# SC = O(N) For Storing the Item Object.
def maximumWeightValue(wt,val,capacity):
    Items = []
    totalValue = 0
    totalWeight = 0

    for i in range(0,len(wt)):
        Items.append(Item(wt[i],val[i]))

    # Sort the Item list with Value / Weight ratio i.e decreasing value of value per weight so that we can pick maximum value first.
    Items = sorted(Items,reverse=True,key = lambda  x : x.value/x.weight)

    for item in Items:

        if totalWeight + item.weight <= capacity:
            totalValue = totalValue + item.value
            totalWeight = totalWeight + item.weight

        else:
            rem_weight = capacity - totalWeight
            y = rem_weight / item.weight
            totalValue = totalValue + (y * item.value)
            totalWeight = totalWeight + (y * item.weight)
            break

    return totalValue


# Driver Code
# wt = [4, 2, 55, 50, 33, 11, 77, 19, 40, 13, 27, 37, 95, 40, 96, 21, 35, 29, 68, 2, 98, 3,
#       18, 43, 53, 7, 2, 31, 87, 42, 66, 40, 45, 20, 41, 30, 32, 18, 98, 22, 82, 26, 10, 28, 68,
#       7, 98, 4, 87, 16, 7, 34, 20, 25, 29, 22, 33, 30, 4, 20, 71, 19, 9, 16, 41,
#       50, 97, 24, 19, 46, 47, 2, 22, 6, 80, 39, 65, 29, 42, 1, 94, 1, 35, 15]
# val = [78, 16, 94, 36, 87, 43, 50, 22, 63, 28, 91, 10, 64, 27, 41, 27, 73, 37, 12, 19, 68, 30, 83, 31,
#        63, 24, 68, 36, 30, 3, 23, 9, 70, 18, 94, 7, 12, 43, 30, 24, 22, 20, 85, 38, 99, 25, 16, 21, 14,
#        27, 92, 31, 57, 24, 63, 21, 97, 32, 6, 26, 85, 28, 37, 6, 47, 30,
#        14, 8, 25, 46, 83, 46, 15, 18, 35, 15, 44, 1, 88, 9, 77, 29, 89, 35]
#
# # 2 55 50 33 11 77 19 40 13 27 37 95 40 96 21 35 29 68 2 98 3 18 43 53 7 2
# # 31 87 42 66 40 45 20 41 30 32 18 98 22 82 26 10 28 68 7 98 4 87 16 7 34 20
# # 25 29 22 33 30 4 20 71 19 9 16 41 50 97 24 19 46 47 2 22 6 80 39 65 29 42 1 94 1 35 15
# capacity = 87

wt = [10,20,30]
val = [60,100,120]
capacity = 50

print("Maximum Value in Knapsack is {}".format(maximumWeightValue(wt,val,capacity)))