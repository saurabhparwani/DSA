# Method to Calculate Minimum Platform required to maintain Arrival / Departure of all the train.
def minimumPlatform(n, arr, dep):
    if n == 0:
        return 0

    minimum = 1
    curr = 1
    arr.sort()
    dep.sort()

    i = 1
    j = 0
    while i < n and j < n:
        if arr[i] > dep[j]:
            curr -= 1
            j += 1
        else:
            curr += 1
            i += 1
        if curr > minimum:
            minimum = curr
    return minimum


# Driver Code.

# TestCase 1
arrival_1 = [900 ,940, 950, 1100, 1500, 1800]
departure_1 = [910, 1200, 1120, 1130, 1900, 2000]
print("Minimum Platforms required {}" .format(minimumPlatform(len(arrival_1),arrival_1,departure_1)))

# TestCase 2

arrival_2 = [900, 1100, 1235]
departure_2 = [1000, 1200, 1240]
print("Minimum Platforms required {}" .format(minimumPlatform(len(arrival_2),arrival_2,departure_2)))