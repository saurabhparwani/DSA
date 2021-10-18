# Problem Statement : https://www.geeksforgeeks.org/reverse-doubly-linked-list-groups-given-size/

pointers = [None]*4

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def printList(self):
        curr = self.head
        while curr:
            print(curr.data,end =  " ")
            curr = curr.next
        print()

    def appendtoList(self,data):

        if self.head == None:
            self.head = Node(data)
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = Node(data)

    def makeList(self,count):
        arr = [3 ,8, 7, 2, 5, 3]
        for i in arr:
            self.appendtoList(i)

    # TC = O(N)
    # SC = O(N) For Recursive Stack
    def reverseInGroups(self,head,k):

        # Base case
        if k < 1 or head is None or head.next is None:
            return head

        count = 1

        prev = None
        curr = head

        length = self.getLength()
        # Reverse the First Group of List.
        while curr and count <= k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
        # If there are more than K elements in the list then call recursively that function for next group.
        length -= k
        if length >= k and next:
            head.next = self.reverseInGroups(next, k)
        else:
            head.next = next

        return prev

    def getLength(self):
        if self.head is None: return 0
        count = 1
        curr = self.head
        while curr:
            curr = curr.next
            count+=1

        return count

    def reverseInGroupsIterative(self,k):

        if self.head is None or self.head.next is None or k < 2:
            return self.head

        length = self.getLength()
        curr = self.head
        next = self.head
        while length >= k:

            count = 0
            for i in range(0,k):
                curr = next
                next = curr.next
                changePointers(curr)

            length -= k

            if pointers[2] is None:
                pointers[2] = pointers[0]
                pointers[3] = pointers[1]
                pointers[0] = pointers[1] = None
            else:
                pointers[3].next = pointers[0]
                pointers[3] = pointers[1]
                pointers[0] = pointers[1] = None

        if next:
            pointers[3].next = next
        else:
            pointers[3].next = None
        return pointers[2]




def changePointers(node):
    if pointers[0] is None:
        pointers[0] = pointers[1] = node
    else:
        node.next = pointers[0]
        pointers[0] = node


# Driver Code
L = LinkedList()
L.makeList(10)
L.printList()

#
L.head = L.reverseInGroups(L.head,2)
# L.head = L.reverseInGroupsIterative(4)
L.printList()