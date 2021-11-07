# Problem Statement : https://practice.geeksforgeeks.org/problems/smallest-number5829/1

def findSmallestNumber(S,D):

    # Check Base Case
    # Case 1 : If it's impossible to build that sum in D digits.
    if 9*D < S:
        return -1

    # Case 2: If Sum is 0 and D > 1 then also it's impossible to make as 00 is equal to 0.
    if S == 0 and D > 1:
        return -1

    arr = [-1]*D

    # Now Fill the Array From last and place maximum number at last index as we are finding the Smallest number.


    # Subtract this 1 from initial Sum as in case of S = 9 & D = 2 We will plce 9 at second place so first place will remain empty but we have to
    # make 2 Digit number that's why we are doing that.
    S = S - 1

    for i in range(D-1,0,-1):
        # If Sum is less greater than 9 then place 9 at the current index.
        if S > 9:
            arr[i] = 9
            S -= 9

        else:
            arr[i] = S
            S = 0

    # Now at this Step we are at the First place of the digit.So add here S+1 at first position.
    # This is to make sure that first element always has something greater than 0 , that's why we subtracted 1 to make it exact D digits.
    arr[0] = S + 1

    answer = ''
    for i in arr:
        answer += str(i)
    return int(answer)




# Driver Code
S = 20
D = 3

print("Smallest Number with given Sum & Digits {}".format(findSmallestNumber(S,D)))