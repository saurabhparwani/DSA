# Class Node
class Node(object):
    # Define Constructor
    def __init__(self,data):
        self.data = data
        self.next = None

# Method to merge two sorted list and this method will return head of the sorted list.
def sortedMerge(left,right):

    # resulting list
    result = None

    # Base Case
    if left == None:
        return right
    if right == None:
        return left

    # Pick Either left's first or right's first element based on the Small element.
    # If element is Smaller or equal to the element in right list
    if left.data <= right.data:
        result = left
        result.next = sortedMerge(left.next,right)

    else:
        result = right
        result.next = sortedMerge(left,right.next)

    return result


# Method for Merge Sort. This Method will first divide the list in two parts . Then it will Sort Left & right Sublist and then merge the Two Sorted List.
def mergeSort(head):

    # Base Case if list is Null or list has only 1 Node.
    if head == None or head.next == None:
        return head

    # Get the middle element of list.
    middle = getMiddleNode(head)

    # Get the next element from middle to apply sort on right sublist.
    next_of_middle = middle.next

    # Break the link of middle node .
    middle.next = None

    # Sort the Left Sublist
    left = mergeSort(head)

    # Sort the right Sublist
    right = mergeSort(next_of_middle)

    # Merge the Sorted Array.
    mergeSorted = sortedMerge(left,right)

    # return the Sorted list
    return mergeSorted

# Method to make a Singly Linked List
def makeSingleLinkList():
    head = Node(8)
    head.next = Node(12)
    head.next.next = Node(6)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(1)
    head.next.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next.next = Node(2)

    return head

# Method to get the middle of the List
def getMiddleNode(head):
    if head :
        fastPtr = head
        slowPtr = head

        while fastPtr.next and fastPtr.next.next:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next

        return slowPtr

    else:
        return None


# Method to Print the List.
def printList(head):
    if head:
        curr = head
        while curr:
            print(curr.data,end = " ")
            curr = curr.next
        print()
    else:
        print("List is Empty")



# Driver Node
head = makeSingleLinkList()

# Print List
printList(head)

head = mergeSort(head)
printList(head)