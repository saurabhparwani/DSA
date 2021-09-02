# Problem Statement  :  https://practice.geeksforgeeks.org/problems/roman-number-to-integer3201/1

# Method to Calculate integer equivalent of roman number.
# TC = O(N) , SC = O(1)
def romanToDecimal(str):
    ma = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    last_char = ''
    total = 0
    for i in str:

        #If next character is small or equal to previous element.
        if last_char == '' or ma[last_char] >= ma[i]:
            total += ma[i]
            last_char = i

        # Else for Cases like IV or IX.
        else:
            total = total - ma[last_char] + (ma[i] - ma[last_char])

    return total