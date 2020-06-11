"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

import sys
import os
sys.path.append(os.path.abspath('../singly_linked_list'))
from singly_linked_list import LinkedList

class Queue(LinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.remove_head()
        else: return None

class Stack(LinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0
        

    def __len__(self):
        return self.size

    def push(self, value):
        self.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.remove_tail()
        else: return None

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not

    ## recurvise
    # def contains(self, target):
    #     if target == self.value:
    #         return True
    #     else:
    #         if target < self.value:
    #             if self.left:
    #                 return self.left.contains(target)
    #         else:
    #             if self.right:
    #                 return self.right.contains(target)
    #     return False

    ## iterative
    def contains(self, target):
        node = self
        while node != None:
            if target > node.value:
                node = node.right
            elif target < node.value:
                node = node.left
            else:
                return True
        return False

    # Return the maximum value found in the tree
    # recursive
    # def get_max(self):
    #     if self.right:
    #         return self.right.get_max()
    #     else:
    #         return self.value

    # iterative
    def get_max(self):
        node = self
        highest = node.value
        while node != None:
            highest = node.value
            node = node.right
        return highest

    # Call the function `fn` on the value of each node
    # recursive
    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        fn(self.value)
        
    
    # iterative
    # def for_each(self, fn):
    #     pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        print(self.value)
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        node_queue = Queue()
        node_queue.enqueue(node)
        while node_queue.size > 0:
            current_node = node_queue.dequeue()
            print(current_node.value)
            if current_node.left:
                node_queue.enqueue(current_node.left)
            if current_node.right:
                node_queue.enqueue(current_node.right)

            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        node_stack = Stack()
        node_stack.push(node)
        while node_stack.size > 0:
            current_node = node_stack.pop()
            print(current_node.value)
            if current_node.left:
                node_stack.push(current_node.left)
            if current_node.right:
                node_stack.push(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
