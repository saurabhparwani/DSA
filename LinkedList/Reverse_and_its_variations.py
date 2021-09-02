# Import Statement to Iport the class frm list
import sys
sys.path.append(".")
from LinkedList.SingleLinkedList import SingleLinkedList
from LinkedList.SingleLinkedList import Node


# Method to reverse a Linked List in size of K .
# Suppose a list is given as 1 2 3 4 5 6 7 8 9 10 then
# If k = 2 : Reverse list = 2 1 4 3 6 5 8 7 10 9
# If k = 3 : Reverse list = 3 2 1 6 5 4 9 8 7 10
# If k = 4 : Reverse list = 4 3 2 1 8 7 6 5 9 10





def reverseListRecusrive(list,node):
    curr = node

    # If Node in Null
    if curr == None: return

    # if Node's next is Null then make current node as head & return as it is last Node
    if curr.next is None :
        list.head = curr
        return

    # Call this same recursive method for next nodes in the list
    reverseListRecusrive(list,curr.next)

    # Set Current Nodes next Node link to current node
    curr.next.next=curr
    curr.next = None   # Break Existing Node
def reversList(list):

    curr = list.get_head_node()
    prev = None

    if curr is None:
        print("List is Empty")
        return
    while curr:
        next = curr.next
        curr.next=prev
        prev = curr
        curr = next
    list1.head = prev

    while curr:
        next= curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

# Create a List Object
list1 = SingleLinkedList()
list2 = SingleLinkedList()
list_3 = SingleLinkedList()

list1.printList()

# Make Linked list of desired nodes & Values
list1.makeLinkedList(10,2)
list1.printList()

list2.makeLinkedList(5,3)

# Reverse Iterative Function
reversList(list1)
list1.printList()
list2.printList()
reverseListRecusrive(list2,list2.get_head_node())
list2.printList()


