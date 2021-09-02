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

def createLinkedLists():
    # Create First Linked List
    root_1 = Node(9)
    root_1.next = Node(9)
    root_1.next.next = Node(9)

    # Create second linked list
    root_2 = Node(1)
    root_2.next = Node(5)
    root_2.next.next = Node(7)

    return root_1,root_2


def reverselist(head):
    if head:
        curr = head
        prev = None
        length = 0

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            length += 1

        return [prev,length]


def sumOfTwoLinkedList(head1,head2):
    if head1 and head2:
        # Reverse Both the list
        r1 = reverselist(head1)
        r2 = reverselist(head2)

        # Initialize Carry and now add both linked list based upon their length.
        carry = 0

        f_head = r1[0]
        s_head = r2[0]

        first_node = f_head
        last_node = s_head
        # For Testing Purpose
        # printlist(f_head)
        # printlist(s_head)

        # If Second list is bigger than first list
        if r1[1] < r2[1]:
            # Traverse till both the list have data
            last_ele = None  # To track the last element so that we can have the last element of final list
            while f_head and s_head:
                data = f_head.data + s_head.data + carry
                s_head.data = data % 10
                carry = data // 10
                last_ele = s_head
                f_head = f_head.next
                s_head = s_head.next

            # Now add remaining element of the larger list
            while s_head:
                data = s_head.data + carry
                s_head.data = data % 10
                carry = data // 10
                last_ele = s_head
                s_head = s_head.next

            #If carry is pending
            while carry!=0:
                last_ele.next = Node(carry%10)
                carry = carry//10
                last_ele = last_ele.next

            return reverselist(last_node)

        else:
            # Traverse till both the list have data
            last_ele = None  # To track the last element so that we can have the last element of final list
            while f_head and s_head:
                data = f_head.data + s_head.data + carry
                f_head.data = data % 10
                carry = data // 10
                last_ele = f_head
                f_head = f_head.next
                s_head = s_head.next

            # Now add remaining element of the larger list
            while f_head:
                data = f_head.data + carry
                f_head.data = data % 10
                carry = data // 10
                last_ele = f_head
                f_head = f_head.next

            # If carry is pending
            while carry != 0:
                last_ele.next = Node(carry % 10)
                carry = carry // 10
                last_ele = last_ele.next

            return reverselist(first_node)


    # If second list is Null
    if head1:
        return head1
    # If first list is Null
    else: return head2

# Driver Method
list_1, list_2 = createLinkedLists()
printlist(list_1)
printlist(list_2)

node = sumOfTwoLinkedList(list_1,list_2)

printlist(node[0])

