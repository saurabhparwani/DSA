# Class Node
class Node(object):
    # Define Constructor
    def __init__(self,data):
        self.data = data
        self.next = None

# Method to make a Singly Linked List
def makeSingleLinkList():
    head = Node(7)
    head.next = Node(58)
    head.next.next = Node(36)
    head.next.next.next = Node(34)
    head.next.next.next.next = Node(16)
    head.next.next.next.next.next = head.next.next
    return head

# Method to Print the List.
# def printList(head):
#     if head:
#         curr = head
#         while curr:
#             print(curr.data,end = " ")
#             curr = curr.next
#         print()
#     else:
#         print("List is Empty")

# Method to check that Loop exist in Singly Linked list through slow & fast ptr.
# Also find the start point of the node.
def isLoopExist(head):
    if head is None:
        print("List is Empty")
        return
    slowPtr = head
    fastPtr = head

    while fastPtr.next and fastPtr.next.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next

        if slowPtr == fastPtr:

            slowPtr = head

            # Just to find the starting Point of the Node.
            while slowPtr != fastPtr:
                slowPtr = slowPtr.next
                fastPtr = fastPtr.next

            print("Start Point of the loop is {}".format(slowPtr.data))
            return True
    return False

# Now the Follow Up Question :  Find the starting point of the loop. 
# So if the loop is found in the linked list then to find the start point we will do following steps.
# 1. Loop Condition is fast_ptr == slow_ptr
# 2. Now again assign fast_ptr = head of linked list and then move both fast & slow pointers by 1 step.
# 3. Now when both Pointer match i.e fastPtr == slowPtr , then that is the start point of the loop.


# Driver Node
head = makeSingleLinkList()

# Print List
# printList(head)

if isLoopExist(head):
    print("Loop exist in linked list")
else:
    print("Loop does not exist in linked list")

