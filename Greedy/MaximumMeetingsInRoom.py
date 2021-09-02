# Problem Statement

# There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) where S[i] is the start time of meeting i and F[i] is finish time of meeting i.
# The task is to find the maximum number of meetings that can be accommodated in the meeting room. Print all meeting numbers.

# Algo
# 1. First We will create list of meeting consisting of meeting object which will have start time , end time and meeting number .  O(N)
# 2. Then We will Sort  the Meeting list based upon their end time. O(NLogN). If the end time of 2 meetings are same then meeting that occurs first
#     will come in sorted list first.
# 3. Then we will traverse complete array to calculate the maximum meeting in a room.

class Meeting(object):
    def __init__(self,start,end,pos):
        self.start = start
        self.end = end
        self.pos = pos

def printMeetingsInRoom(start,end):

    # Make List of Meeting object based upon their Position and sort them based on their end time.
    meetings = []

    n = len(start)
    for i in range(0,n):
        meetings.append(Meeting(start[i],end[i],i+1))

    # Sort the Meeting List
    meetings.sort(key= lambda x:x.end)

    # Traverse the Meeting array and check that if starting time of any meeting is greater than ending time of previous meeting then we can perform the meeting.

    current_ending = -10000

    i =0
    while i < n :
        meeting = meetings[i]

        if meeting.start > current_ending :
            print(meeting.pos,end=" ")
            current_ending = meeting.end

        i+=1



# Driver Code

start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]
printMeetingsInRoom(start,end)