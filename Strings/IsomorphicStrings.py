# Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.
# Two strings str1 and str2 are called isomorphic if there is a one to one mapping possible for every character of str1 to every character of str2 while preserving the order.
# Note: All occurrences of every character in ‘str1’ should map to the same character in ‘str2’

# Input:
# str1 = aab
# str2 = xxy
# Output: 1
# Explanation: There are two different charactersin aab and xxy, i.e a and b with frequency 2and 1 respectively.

# Input:
# str1 = aab
# str2 = xyz
# Output:
# Explanation: There are two different charactersin aab but there are three different
# charactersin xyz.So there won 't be one to one mapping between str1 and str2.

# Input :
# rfkqyuqf
# jkxyqvnr
# Correct Output : 0

# Method to check that whether two strings are isomorphic or not.
def isIsoMorphic(a,b):
    if len(a) != len(b):
        return False

    map = [-1]*256
    used = [False]*256
    for i in range(0,len(a)):
        # Character from first string is visited first time.
        if map[ord(a[i])] == -1:
            # To check that character at same place in another string is already used or not.
            # If it is already used than return False as it is not one to one mapping.
            if used[ord(b[i])] == True:
                return False

            # Else Mark that second string char as visited & link that char with char in first string.
            map[ord(a[i])] = ord(b[i])
            used[ord(b[i])] = True

        # Else Character from first string is already seen check whether it has same mapping in str 2.
        else:
            if map[ord(a[i])] != ord(b[i]):
                return False

    return True

# Driver Method 

str1 = 'rfkqyuqf'
str2 = 'jkxyqvnr'

if isIsoMorphic(str1,str2):
    print("Strings are Isomorphic")
else:
    print("Strings are not Isomorphic")