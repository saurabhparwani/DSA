# Problem Statement : https://www.geeksforgeeks.org/snake-ladder-problem-2/


# A Single Point to represent a location in Board which points to distance & steps to reach that distance.
class Point(object):
    def __init__(self,distance=0,step=0):
        self.distance = distance
        self.step = step


def minimumDiceThrows(move,N):
    # Make a visited array to store all the visited Points.
    visited = [False] * N
    queue = []

    # Mark the First Node as the Visited Node & Add it to the Queue.
    visited[0] = True
    queue.append(Point(0,0))    # Steps will be 0 as initially it will be present at 0.


    # Now traverse the Queue while Q is not empty in BFS Manner.
    while queue:

        curr = queue.pop(0)
        dist = curr.distance

        # If the destination of the popped node is the destination we want then we are done , no need to test further.
        if dist == N-1:
            break

        # Now Traverse the next points adding 1 to 6( Dice has number from 1 to 6) , If cell is Unvisited then add it in the Queue with increased step.
        j = dist + 1

        # Check next 6 points and boundary condition that we don't cross the chessboard.
        while j <= dist + 6 and j < N:

            # If Next location is Unvisited then add it to Queue.
            if visited[j] == False:
                newPoint = Point()
                newPoint.step = curr.step + 1

                visited[j] = True   # Mark this Point as visited
                # If Current Point is not Snake or ladder then go to the Location where Ladder or snake is taking else J.
                if move[j] != -1:
                    newPoint.distance = move[j]
                else:
                    newPoint.distance = j

                #  Add it to the Queue.
                queue.append(newPoint)

            j += 1

    if curr:
        return curr.step
    return 0


# Driver Code
N = 30
moves = [-1] * N

# Ladders
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28

# Snake
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6

print("Minimum dice Throws {}".format(minimumDiceThrows(moves,N)))