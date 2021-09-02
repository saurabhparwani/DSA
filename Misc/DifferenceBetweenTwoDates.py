# Program to find the difference between two dates.
# We will calculate days from 00/00/0000 to first date let's call that n1 & diff from 00/00/0000 to second date let's call that n2.
# Then we will simply return the diff between n2-n1 and that will be our answer.

class Date(object):

    # Constructor
    def __init__(self,day,mon,year):
        self.day = day
        self.mon = mon
        self.year = year


months = [31,28,31,30,31,30,31,31,30,31,30,31]

# Method to get number of leap years
def getLeapYears(date):

    year = date.year

    if date.mon <= 2:
        year-=1

    ans = int(year / 4)
    ans += int(year/400)
    ans -= int(year/100)

    return  ans


# Method to get diff between two dates

def getDifferenceBetweenTwoDates(dt1,dt2):

    # Calculate Days for n1.
    n1 = dt1.year * 365 + dt1.day

    for i in range(0,dt1.mon-1):
        n1 += months[i]

    n1 += getLeapYears(dt1)

    # Calculate Days for n2.
    n2= dt2.year*365 + dt2.day

    for i in range(0,dt2.mon-1):
        n2 += months[i]

    n2 += getLeapYears(dt2)

    return n2-n1

# Driver Code

dt1 = Date(1, 2, 2000)
dt2 = Date(1, 2, 2004)
print("Difference between two dates is ",getDifferenceBetweenTwoDates(dt1, dt2))

