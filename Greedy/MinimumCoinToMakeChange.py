# Given a value V, if we want to make a change for V Rs, and we have an infinite supply of each of the denominations in Indian currency, i.e.,
# we have an infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, what is the minimum number of coins and/or notes needed to make the change ?
#
# Example
#
# Input: V = 70
# Output: 2
# We need a 50 Rs note and a 20 Rs note.
#
# Input: V = 121
# Output: 3
# We need a 100 Rs note, a 20 Rs note and a 1 Rs coin.

global N
N = 9
coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

def findMinCoin(value):
    if value <= 0:
        print("No Coin Required")

    ans = []
    min_coin = 0
    i = N-1

    # Loop till we collect complete amount.
    while value != 0:

        # Collect Coins till the Value is greater than current denomination.
        while value >= coins[i]:
            min_coin += 1
            value -= coins[i]
            ans.append(coins[i])
        i -= 1

    print("Minimum Coins Required {}".format(min_coin))
    print(ans)

n  = int(input("Enter a Value :\n"))
findMinCoin(n)
