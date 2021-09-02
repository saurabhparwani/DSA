# Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1?
# (eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false).

# Method to check whether two strings are rotation of each other or not.
# TC : It depends on the String Matching Algorithm.
# If implementation of strstr is done using KMP matcher then complexity of the above program is (-)(n1 + n2) where n1 and n2 are lengths of strings.
# KMP matcher takes (-)(n) time to find a substrng in a string of length n where length of substring is assumed to be smaller than the string.

def areRotations(str1,str2):
    # Check that length of both strings is equal or not.
    if len(str1) != len(str2):
        return False

    # Create a temporary string.
    temp = str1 + str1
    # Now check that whether that string2 is substring  of temporary string or not.
    # If it's not a substring then str2 is not rotation of str 1.
    if (temp.count(str2)) > 0:
        return True
    else:
        return False

# Driver program to test the above function
string1 = "AACD"
string2 = "ACDA"

if areRotations(string1, string2):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations of each other")