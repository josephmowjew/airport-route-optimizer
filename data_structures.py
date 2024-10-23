
class Node:
    """Basic node structure for linked list implementation"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """Custom Queue implementation using linked list"""
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return item
    
    def is_empty(self):
        return self.front is None
    
    def size(self):
        return self._size

class Stack:
    """Custom Stack implementation using linked list"""
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self._size