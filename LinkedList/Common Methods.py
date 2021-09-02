class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = next


# Problem Statements
# 1. Intersection Point in Y Shapped Linked Lists
# https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1

# Function to find intersection point in Y shaped Linked Lists.
# TC = O(M+N) where M & N length of both linked list , SC  =  O(1)
def intersetPoint(head1, head2):
    len_a = 0
    len_b = 0
    pt_1 = head1
    pt_2 = head2

    # Find Length of both Linked lists
    while head1 and head2:
        len_a += 1
        len_b += 1
        head1 = head1.next
        head2 = head2.next
    while head1:
        len_a += 1
        head1 = head1.next
    while head2:
        len_b += 1
        head2 = head2.next

    # Now traverse extra spaces in the linked list so that length of remaining list is same as shorter list.
    if len_a < len_b:
        for i in range(0, len_b - len_a):
            pt_2 = pt_2.next
    else:
        for i in range(0, len_a - len_b):
            pt_1 = pt_1.next

    # Check for Common node Case.
    while pt_1 and pt_2:
        if pt_1 == pt_2 and pt_1.data == pt_2.data:
            return pt_1.data

        pt_1 = pt_1.next
        pt_2 = pt_2.next

    return -1


# Intersection of two sorted Linked lists
# 2. https://practice.geeksforgeeks.org/problems/intersection-of-two-sorted-linked-lists/1#

# Function to find intersection of two sorted linked list.
# TC = O(Min(M,N)) as we are finding common ele in both list. , SC = O(N) For creating new Linked list.
def findIntersection(head1, head2):
    front = rear = None

    # Traverse till both list are non null.
    while head1 and head2:

        # If common data found then create a new list.
        if head1.data == head2.data:
            if front is None and rear is None:
                front = rear = Node(head1.data)

            else:
                rear.next = Node(head1.data)
                rear = rear.next

            head1 = head1.next
            head2 = head2.next

        # Else traverse the linked list whose element is less.
        elif head1.data < head2.data:
            head1 = head1.next

        else:
            head2 = head2.next

    # Return the head node of new List.
    return front


# Function to find Nth node from the end of a linked list.
# https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
# This Code is O(N) but in two pass . Use two pointer technique to do this in one pass.
def getNthNodeFromLast(head, n):
    length = 0
    curr = head
    # Find the length of th linked list.
    while curr:
        length += 1
        curr = curr.next

    # If n > length of the list then return -1 else find the Length - nth node from the beginning.
    if n > length:
        return -1
    else:
        curr = head
        i = 1
        while i <= length - n:
            curr = curr.next
            i += 1
        return curr.data

    # Recursive Method for the above approach.
    # void printNthFromLast(struct Node * head, int n)
    # {
    #     static int i = 0;
    #     if (head == NULL)
    #          return;
    #     printNthFromLast(head->next, n);
    #     if (++i == n)
    #        cout << head->data;
    # }

# Method to find Nth Node from end using two pointer's technique.
# TC = O(N) and in single pass.
def getNthFromLast(head, n):
    if head is None:
        return -1

    slow = head
    fast = head
    i = 1
    while i <= n and fast:
        i += 1
        fast = fast.next

    if i > n and fast == None:
        return head.data

    if fast is None:
        return -1

    else:
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.data



# Method to remove duplicates elements from the sorted linkedlist.
# Problem Statement : https://www.geeksforgeeks.org/remove-duplicates-from-a-sorted-linked-list/
# TC = O(N) , SC = O(1)
def removeDuplicatesFromSorted(head):

    if head:
        prev = head
        curr = head.next
        while curr:
            # If curr data is not equal to previous data then only add it to the list
            if curr.data != prev.data:
                prev.next = curr
                prev = curr
            curr = curr.next
        # Once the list is done then set prev.next = None as there can be duplicates in last.
        prev.next = None
        return head

def removeDuplicateFromSorted_Recursive(head):
    # Base Case
    if head == None: return

    if head.next != None:
        if head.data == head.next.data:
            to_free = head.next
            head.next = head.next.next
            removeDuplicateFromSorted_Recursive(head)
        else:
            removeDuplicateFromSorted_Recursive(head.next)

        return head

# # Method to remove duplicates elements from the Unsorted linkedlist.
# Problem Statement : https://www.geeksforgeeks.org/remove-duplicates-from-an-unsorted-linked-list/
def removeDuplicates(self, head):
    if head:
        hash_map = set()
        prev = head
        hash_map.add(head.data)
        curr = head.next
        while curr:
            if not curr.data in hash_map:
                hash_map.add(curr.data)
                prev.next = curr
                prev = curr
            curr = curr.next
        prev.next = None

        return head


# To Check that given linked list is Palindrome or not.
# Problem Statement : https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/
# TC = O(N) , SC = O(1)
class Solution:
    def printList(self, head):
        while head:
            print(head.data, end=" ")
            head = head.next
        print()

    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            ne = curr.next
            curr.next = prev
            prev = curr
            curr = ne

        return prev

    def isPalindrome(self, head):

        slow = head
        fast = head
        l_type = 0

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        middle = slow
        if fast.next is None:
            l_type = 0
        elif fast.next.next is None:
            l_type = 1

        middle.next = self.reverse(middle.next)
        # self.printList(head)

        temp = None
        slow = head
        fast = middle.next
        if l_type == 0:
            temp = middle
        elif l_type == 1:
            temp = fast

        while slow != temp and fast:
            if slow.data != fast.data:
                return False

            slow = slow.next
            fast = fast.next

        return True