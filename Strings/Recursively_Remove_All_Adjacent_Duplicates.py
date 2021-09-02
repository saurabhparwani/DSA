# Given a string, recursively remove adjacent duplicate characters from the string.
# The output string should not have any adjacent duplicates. See following examples.
# Examples:
# Input: azxxzy
# Output: ay
# First “azxxzy” is reduced to “azzy”.
# The string “azzy” contains duplicates,
# so it is further reduced to “ay”.
# Input: geeksforgeeg
# Output: gksfor
# First “geeksforgeeg” is reduced to
# “gksforgg”. The string “gksforgg”
# contains duplicates, so it is further
# reduced to “gksfor”.
# Input: caaabbbaacdddd
# Output: Empty String
# Input: acaaabbbacdddd
# Output: acac

# Helper method to convert list into String.
def toString(x):
    return ''.join(x)

# Helper method to convert string into list.
def toList(str):
    x = []
    for s in str:
        x.append(s)
    return x

# Utility method to remove the adjacent duplicates from the string.
# Start from the leftmost character and remove duplicates at left corner if there are any.
# The first character must be different from its adjacent now. Recur for string of length n-1 (string without first character).
# Let the string obtained after reducing right substring of length n-1 be rem_str. There are three possible cases
# If first character of rem_str matches with the first character of original string, remove the first character from rem_str.
# If remaining string becomes empty and last removed character is same as first character of original string. Return empty string.
# Else, append the first character of the original string at the beginning of rem_str.
# Return rem_str.

def removeUtil(str,last_removed):

    # Base Case when Length of the string is only 1 or 0.
    if len(str) == 0 or len(str) == 1:
        return str

    # If the first character & Second character is same then remove the first character from string till both becomes different or length becomes 1.
    if str[0] == str[1]:
        last_removed = ord(str[0])
        # print(str[0],str.index(str[0]))
        # print(str,2)
        while len(str) > 1 and str[0] == str[1]:
            str = str[1:]
        # At this point first & second char are different in both the strings so now process for substring starting from 2nd char.
        str = str[1:]
        # print(str,9)
        return removeUtil(str,last_removed)


    # At this Point we know that first & second char is not same so test the remaining string.
    rem_str = removeUtil(str[1:],last_removed)
    # print(rem_str,3)

    # Check for first Point.
    # If the rem_str length is not empty and first char of rem_str matches with first char of str. Remove the first char from rem_str.
    if len(rem_str) != 0 and rem_str[0] == str[0]:
        last_removed = str[0]
        return  rem_str[1:]

    # Check for second Point.
    # If the length of rem_str is 0 and the last removed char is equal to first Character of original string.
    if len(rem_str) == 0 and last_removed == ord(str[0]):
        return rem_str

    # Else Append the original string's first character at the start of rem_str and return this.
    return [str[0]]+rem_str

# Method to remove duplicates recursively from string . This method will work as a wrapper method to the recursive method.
def remove(string):
    last_removed = 0
    return  toString(removeUtil(toList(string),last_removed))


# Iterative Method to remove adjacent duplicates from string using stack.
def removeDupicates(str):
    stack = []
    last_removed = 0
    n = len(str)
    for i in range(n):
        if (len(stack) == 0 and last_removed != ord(str[i])) or ( stack[-1] != str[i] and last_removed != ord(str[i])):
            stack.append(str[i])
        elif stack[-1] == str[i]:
            last_removed = ord(stack[-1])
            stack.pop()
    return ''.join(stack)




# Driver Method
string1 = "acbbcddc"
print(remove(string1))
print(removeDupicates(string1))

