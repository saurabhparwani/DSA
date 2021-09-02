# Problem Statement : https://www.geeksforgeeks.org/implement-stack-using-queue/
from queue import Queue

# Approach First. Making Push Operation Costly and Pop operation efficient.
class Stack_1(object):
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.size = 0

    # Insert new element in the Queue such that newly added element is always at the front of the Queue 1.
    def push(self,item):
        # Push the element into Q2.
        self.q2.put(item)
        self.size +=1
        # De queue all the item from Q1 and enqueue into the  Q2.
        while not self.q1.empty():
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        # Swap the Q1 name with the Q2.
        self.q1,self.q2 = self.q2,self.q1

    def pop(self):
        if self.size == 0:
            print("Stack is Empty")
            return
        print("Popped Item from Stack {}".format(self.q1.queue[0]))
        self.q1.get()
        self.size -= 1


# Approach Second. Making Push Operation efficient and Pop operation costly.
class Stack_2(object):
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.size = 0

    # Simply append itm
    def push(self,item):
        self.q1.queue.append(item)
        self.size+=1

    # De queue every item from Q1 except last item and return last item.
    # Swap the names of Q1 & Q2.
    def pop(self):
        if self.q1.empty():
            print("Stack is Empty")
            return

        temp = self.size
        while temp > 1:
            self.q2.put(self.q1.queue[0])
            self.q1.get()
            temp -= 1
        # Last item of the Q1 to be Popped.
        print("Popped Item from stack is {}".format(self.q1.queue[0]))
        self.q1.get()
        self.size -= 1

        # Swap the names
        self.q1,self.q2 = self.q2,self.q1


# Driver Method
stack = Stack_2()
stack.push(10)
stack.push(15)
stack.pop()
stack.push(20)
stack.push(30)
stack.pop()
stack.pop()
stack.pop()
stack.pop()

