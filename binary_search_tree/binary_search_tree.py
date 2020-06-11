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
sys.path.append(os.path.abspath('../doubly_linked_list'))
from doubly_linked_list import DoublyLinkedList, ListNode

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
        node.for_each(print)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
