# Problem Statement :  https://www.geeksforgeeks.org/queue-using-stacks/

# Method 1 : Make Enqueue operation costly & dequeue operation efficient.
#
# Method 2 : Make Enqueue operation efficient & dequeue operation costly.
#
# Between both the methods method 2 is  more efficient.

# Implement Stacks Using two queues via method 2 .
# TC = Enqueue = O(1) , Dequeue = O(N) , SC = O(N)
class Queue(object):
    # Define Constructor with two stacks.
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # Define Enqueue Operation TC = O(1)
    def enQueue(self,item):
        self.s1.append(item)

    # Define Dequeue Operation TC = O(N)
    # If the stack 1 & stack 2 both are empty then return -1 i.e Queue is Empty.
    # If the stack 2 is empty then Pop all the elements from the stack 1 & push it to stack 2 and then return the top of the stack 2.
    # If the stack 2 is not empty then simply pop the top of the stack 2 and return.

    def deQueue(self):

        # If both the stacks are empty.
        if len(self.s1) == 0 and len(self.s2) == 0:
            print("Queue is Empty")
            return

        # If stack 2 is empty, then pop and push all ele from stack1 to 2 and then return top of the stack2.
        elif len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1[-1])
                self.s1.pop()

            item = self.s2.pop()
            return item

        # If stack 2 is not empty then simply pop and return the top element of the stack2.
        else:
            item = self.s2.pop()
            return item


#    Queue can also implemented Using One stack . It just  that in DeQueue operation pop element recursively and
#   again insert the element into stack.

class QueueUsingSingleStack(object):
    def __init__(self):
        self.stack = []

    def enQueue(self,item):
        self.stack.append(item)

    def deQueue(self):
        if len(self.stack) == 0:
            print("Queue is Empty")
            return

        # Pop the top item
        x = self.stack.pop()

        # If stack has only one element then return that element don't call recursively.
        if len(self.stack) <= 0:
            return x

        # Call Recursively dequeue Method
        item = self.deQueue()

        # Append again popped item.
        self.stack.append(x)

        return item

# Driver Code
# q = Queue()
# q.enQueue(1)
# q.enQueue(3)
# q.enQueue(4)
# print(q.deQueue())
# print(q.deQueue())
# q.enQueue(10)
# print(q.deQueue())
# print(q.deQueue())
# print(q.deQueue())

#-------------------------------#

q = QueueUsingSingleStack()
q.enQueue(23)
q.enQueue(6)
q.enQueue(4)
print(q.deQueue())
print(q.deQueue())
q.enQueue(10)
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
