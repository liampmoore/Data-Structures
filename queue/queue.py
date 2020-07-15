"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop(0)

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.add_to_tail(value)

#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.remove_head()

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size
        
    def enqueue(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        elif self.head is self.tail:
            self.head.next = Node(value)
            self.tail = self.head.next
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self):
        value = None
        if self.size == 0:
            return None
        else:
            self.size -= 1
            if self.head is self.tail:
                value = self.head.value
                self.head = None
                self.tail = None
            else:
                value = self.head.value
                self.head = self.head.next
            return value