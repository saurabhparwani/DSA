# Problem Statement : https://www.geeksforgeeks.org/flattening-a-linked-list/

class Node(object):
    def __init__(self,data):
        self.data = data
        self.right = None
        self.down = None

class LinkedList():

    def __init__(self):
        # head of list
        self.head = None

    def push(self,head_ref,data):

        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(data)

        # Make next of new Node as head
        new_node.down = head_ref

        # 4. Move the head to point to new Node
        head_ref = new_node

        # 5. return to link it back
        return head_ref

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end = " ")
            temp = temp.down

    def merge(self,a,b):

        # if first linked list is empty then second is the answer
        if a == None:
            return b

        # if second linked list is empty then first is the result
        if b == None:
            return a

        # To store the resultant list.
        result = None

        # compare the data members of the two linked lists and put the larger one in the result
        if a.data < b.data:
            result = a
            result.down = self.merge(a.down,b)

        else:
            result = b
            result.down = self.merge(a,b.down)

        result.right = None
        return  result

    # TC = O(N) We are only traversing list.
    # SC = O(N) For stack space & to create the merged list.
    def flattenList(self,root):

        # Base Case
        if root is None or root.right is None:
            return root

        # recur for list on right
        root.right = self.flattenList(root.right)

        # now merge
        root = self.merge(root,root.right)

        # return the root it will be in turn merged with its left
        return root

# Method to create a linked list.
def makeList(L):
    L.head = L.push(L.head, 30);
    L.head = L.push(L.head, 8);
    L.head = L.push(L.head, 7);
    L.head = L.push(L.head, 5);

    L.head.right = L.push(L.head.right, 20);
    L.head.right = L.push(L.head.right, 10);

    L.head.right.right = L.push(L.head.right.right, 50);
    L.head.right.right = L.push(L.head.right.right, 22);
    L.head.right.right = L.push(L.head.right.right, 19);

    L.head.right.right.right = L.push(L.head.right.right.right, 45);
    L.head.right.right.right = L.push(L.head.right.right.right, 40);
    L.head.right.right.right = L.push(L.head.right.right.right, 35);
    L.head.right.right.right = L.push(L.head.right.right.right, 20);

# Driver Code
L = LinkedList()
makeList(L)

# Flatten the Linked list
L.head = L.flattenList(L.head)

# Print the list
L.printList()

