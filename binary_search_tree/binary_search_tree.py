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
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        
    
    # iterative
    # def for_each(self, fn):
    #     pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # First check if there is a node to the left, if so prioritize executing this function on that node first
        if node.left:
            node.left.in_order_print(node.left)
        # Then visit the current node on the current function call
        print(self.value)
        # Then check if there is a node to the right, and if so, call this function on that node and it's children
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        # Create the queue and add the first node
        print_queue = Queue()
        print_queue.enqueue(node)

        # While the queue is greater than zero
        while print_queue.size > 0:

            # The current node equals the first item in the queue, and the item is removed from the front of the queue
            current_node = print_queue.dequeue()
            # Do whatever it is you must do to the node, visit, check for base condition, execute callback, modify value, etc.
            print(current_node.value)

            # If there is a left node add it to the end of the queue
            if current_node.left:
                print_queue.enqueue(current_node.left)
            # If there is a right node add it to the end of the queue
            if current_node.right:
                print_queue.enqueue(current_node.right)
            
            # Now the next node in the current row will be up first in the queue
            # and the next row will be lined up in order from left to right after the items in the current row

            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Create the stack and add the first node
        print_stack = Stack()
        print_stack.push(node)

        # While the stack length is greater than zero
        while print_stack.size > 0:

            # Change the current node to node on the top/end of the stack, and remove that node from the top of the stack
            current_node = print_stack.pop()
            # Do whatever it is you must do to the node, visit, check for base condition, execute callback, modify value, etc.
            print(current_node.value)

            # If there is a left node add it to the top of the stack
            if current_node.left:
                print_stack.push(current_node.left)
            # If there is a right node add it to the top of the stack
            if current_node.right:
                print_stack.push(current_node.right)

            # Now the left node beneath the current node will be up next, on top of the stack
            # and if that first node has another node to the left below it, that will be placed on the stack
            # the stack will only get to the right current node once the full extent of left nodes has been visited

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if node.left:
            node.left.pre_order_dft(node.left)
        if node.right:
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.left.post_order_dft(node.left)
        if node.right:
            node.right.post_order_dft(node.right)
        print(self.value)
        
