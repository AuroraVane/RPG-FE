class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    #Initializing a stack
    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def peek(self):
        #Sanity check to empty stack
        if self.isEmpty():
            return None
        return self.head.data
    
    def push(self, value):
        node = Node(value)
        node.next = self.head #Push the stack deeper
        self.head = node #Make the new node the head
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return None
        remove = self.head
        self.head = self.head.next
        self.size -= 1
        return remove.data
