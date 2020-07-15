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
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
        else:
            if self.right:
                return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)
        fn(self.value)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while len(q) > 0:
            node = q.dequeue()
            if node.left:
                q.enqueue(node.left)
            
            if node.right:
                q.enqueue(node.right)
            print(node.value)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)
        while len(s) > 0:
            node = s.pop()
            if node.left:
                s.push(node.left)
            if node.right:
                s.push(node.right)
            print(node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.pre_order_dft(node.left)
        if node.right:
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.post_order_dft(node.left)
        if node.right:
            node.post_order_dft(node.right)
        print(node.value)