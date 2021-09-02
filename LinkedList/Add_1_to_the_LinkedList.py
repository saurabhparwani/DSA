class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
def printlist(root):
    if root:
        while root:
            print(root.data,end = " ")
            root = root.next
        print()
    else:print("List is Empty")


def reverslist(root):
    prev = None
    current = root
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return  prev

def reverslist_Recursive(root):
    if root is None:return root
    if root.next is None:
        return root
    head = reverslist_Recursive(root.next)
    root.next.next = root
    root.next  = None
    return  head

def addOnetoLinkedListItreative(root):
    if root:

        # reverse the given link list first
        reverse_list_head  = reverslist(root)
        curr = reverse_list_head
        carry = 0
        flag = True
        prev = None

        # Add 1 to 1st Node
        curr.data += 1

        # Traverse every element of linked list with a carry variable
        while curr:
            num = curr.data+carry
            curr.data = num % 10
            carry = num//10
            prev = curr
            curr = curr.next

        # If there is carry remaining create new node
        while carry:
            node = Node(carry%10)
            prev.next = node

        # Again reverse the link list
        reverse_list_head = reverslist(reverse_list_head)
        return reverse_list_head

    else:
        node = Node(1)
        return  node


def addOneRecusrive(root):
    if root is None: return  0
    if root.next == None:
        num = root.data + 1
        root.data = (num) %10
        carry = num // 10
        return carry

    carry = addOneRecusrive(root.next)
    num =  root.data + carry
    root.data = num % 10
    return num // 10


root = Node(9)
root.next = Node(9)
root.next.next = Node(9)
printlist(root)
# node = addOnetoLinkedListItreative(root)
# printlist(node)

carry = addOneRecusrive(root)
if carry == 1 :
    newnode = Node(1)
    newnode.next = root
    printlist(newnode)
else:
    printlist(root)