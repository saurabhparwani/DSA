# Problem Statement : https://www.geeksforgeeks.org/minimum-swap-required-convert-binary-tree-binary-search-tree/
# Similar Question : https://www.geeksforgeeks.org/minimum-swap-required-convert-binary-tree-binary-search-tree/

# Method 1 : Using Selection Sort , TC = O(N*N) , SC = O(1)

# Method 2 : Using Sorting & Hashmap
# TC = O( NLogN ) SC = O(N).
def minimumSwaps(arr,n):

    ans = 0
    temp = arr.copy()
    temp.sort()

    h = {}   # Store the index of every element in the Hash map.
    for i in range(n):
        h[arr[i]] = i

    # Now Traverse the array.
    for i in range(n):
        # If element is not present at the right position then swap it with it's right position in the array.
        if arr[i] != temp[i]:
            # Store the element & Swap the element with the correct element.
            init = arr[i]

            arr[i],arr[h[temp[i]]] = arr[h[temp[i]]],arr[i]
            ans += 1

            # Now Update the Elements in the Hash map.
            h[init]  = h[temp[i]]
            h[temp[i]] = i

    return ans


# Method 3 : Using Graph Cycle
# TC = O(NLogN) SC = O(N)
def minimumSwaps_Cycle(arr,n):

    # Create a new Array with its pair of element & it's position in the array.
    array_with_position = []
    for i in range(n):
        array_with_position.append((i,arr[i]))

    # Sort this array depending upon the array element in the array.
    array_with_position.sort(key = lambda it:it[1])

    # To keep the track of visited element.
    visited = [False]*n

    answer = 0

    # Now traverse the array and find cycles in the array.
    for i in range(n):

        # If element is already visited/swapped or it is at the correct position then continue.
        if visited[i] or array_with_position[i][0] == i:
            continue

        # Else find the number of elements in the cycles.
        cycle_size = 0
        j = i

        while not visited[j]:
            # Mark this element
            visited[j] = True

            # go to the next node in the cycle.
            j = array_with_position[j][0]
            cycle_size = cycle_size + 1

        # Update the answer
        answer += (cycle_size -1 )

    return answer # return the answer




# Driver Code
arr = [1, 5, 4, 3, 2]
arr2 = [1, 5, 4, 3, 2]

print("Minimum number of swaps to sort the array {}".format(minimumSwaps(arr,len(arr))))
print("Minimum number of swaps to sort the array {}".format(minimumSwaps_Cycle(arr2,len(arr2))))

