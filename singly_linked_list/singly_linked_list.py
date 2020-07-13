class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        elif self.head is self.tail:
            self.head.next = Node(value)
            self.tail = self.head.next
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def remove_head(self):
        value = None
        if not self.head:
            return None
        elif self.head is self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
        else:
            value = self.head.value
            self.head = self.head.next
        return value

    def remove_tail(self):
        value = None
        if self.head is None:
            return None
        elif self.head is self.tail:
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

    def contains(self, value):
        if not self.head:
            return None
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False


    def get_max(self):
        if not self.head:
            return None
        current = self.head
        max_value = self.head.value
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value