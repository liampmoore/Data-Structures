"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop()


class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        elif self.head is self.tail:
            self.head.next = Node(value)
            self.tail = self.head.next
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            if self.head is self.tail:
                value = self.head.value
                self.head = None
                self.tail = None
            else:
                value = self.tail.value
                current = self.head
                while(current.next is not self.tail):
                    current = current.next
                current.next = None
                self.tail = current
            return value
            