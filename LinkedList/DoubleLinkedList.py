# Node class to represent a single node in DLL.

# Programs to be done with this Code.
# 1. https://www.geeksforgeeks.org/find-pairs-given-sum-doubly-linked-list/


class Node(object):
    def __init__(self,data):
        self.data = data
        self.nexr = self.prev = None



# Utility Method to reverse a DLL.
# TC = O(N) , SC = O(1)
def reverseDLL(node):
    if node:

        curr = node
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next

        return curr

