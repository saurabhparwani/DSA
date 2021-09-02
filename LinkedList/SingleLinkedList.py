# Node Class which represent a single Node
class Node(object):
    def __init__(self):
        self.data=None
        self.next=None

    def __init__(self,data):
        self.data=data
        self.next=None

    def setData(self,data):
        self.data=data

    def getData(self):
        return self.data

    def setNext(self,Node):
        self.next=Node

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next!=None

# Linked List Class whose Object will be a singly linked list.
class SingleLinkedList(object):

    def __init__(self):
        self.head=None
        self.length=0

    # Get Length of a linked list
    def getLength(self):
        return self.length

    # Get Head of a linked List
    def get_head_node(self):
        return  self.head

    # Method to make a Linked list with N number of nodes in multiple of C.
    def makeLinkedList(self,n,c):
        if n ==0 or c==0:
            print("Enter Non Zero Positive number of N , C")
            return
        for i in range(1,n+1):
            self.insertNode(Node(i*c))

    # Print the Linked List
    def printList(self):
        if self.length==0:
            print("List is Empty")
            return
        node=self.head
        while node!=None:
            print(node.data,end=" ")
            node=node.getNext()
        print("")

    # Insert a Node at the end of the linked List
    def insertNode(self,Node):
        if self.head == None:
            self.head=Node
            self.head.setNext(Node.getNext())
            self.length+=1
        else:
            node=self.head
            while node.getNext() !=None:
                node=node.getNext()
            node.setNext(Node)
            self.length += 1

    # Insert a node at the beginning of the List.
    def insertAtBeginning(self, Node):
        if self.head == None:
            self.head = Node
            self.head.setNext(Node.getNext())
            self.length += 1
        else:
            Node.setNext(self.head)
            self.head = Node
            self.length += 1

    # Insert a Node at given Position
    def insertAtPosition(self,Node,pos):

        if pos <= 0 or pos >(self.length+1):
            print("Enter Proper Position Value")
            return
        else:
            node=self.head
            count=1
            while count<pos-1:
                count+=1
                node=node.getNext()
            if pos==1:
                Node.setNext(node)
                self.head=Node
            else :
                Node.setNext(node.getNext())
                node.setNext(Node)
            self.length+=1

    # Delete Node at Specified Location
    def deleteElementAtPosition(self, pos):
        if self.length == 0:
            print("List is Empty")
            return
        if pos <= 0 or pos > self.length:
            print("Enter proper Position ")
            return
        node = self.head
        count = 1
        while count < pos - 1:
            node = node.getNext()
            count += 1
        if pos == 1:
            self.head = node.getNext()
        else:
            node.setNext(node.getNext().getNext())
        self.length -= 1


    # Find the middle Node of the LinkedList.

    def printMiddleElement(self):
        if self.head is None:
            print("List is Empty")
            return
        slowPtr = self.head
        fastptr = self.head

        # Traverse till we can access the nodes.
        while fastptr.getNext() and fastptr.getNext().getNext():
            fastptr = fastptr.getNext().getNext()
            slowPtr = slowPtr.getNext()

        print("Middle Element of the Linked list is "+str(slowPtr.getData()))

    # Problem Statement : Write a Program to Move the last element to Front in a Linked List.
    # TC = O(N) , SC = O(1)
    def moveLastNodetoFirst(self):

        tmp = self.head
        sec_last = None

        # If list is None or has only one node.
        if not (tmp and tmp.getNext()):
            return

        while tmp.getNext():
            sec_last = tmp
            tmp = tmp.getNext()

        # Now Store the Next of sec_last Node to None.
        # Point head node as next node of last node.
        # Now set last node as new head of the linked list.

        sec_last.setNext(None)
        tmp.setNext(self.head)
        self.head = tmp



list = SingleLinkedList()
list.makeLinkedList(2,8)
list.printList()
list.printMiddleElement()
list.moveLastNodetoFirst()
list.printList()


