# Implement linkedlist with following operations:
# 1. Prepend a value at the beginning of the list
# 2. Append a value at the end of the list
# 3. Search for a node with given value
# 4. Remove the first occurance of a node with given value
# 5. Pop - Return the first node's value and remove it from the list
# 6. Insert value at a given position in the list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        # TODO: Write function to prepend here
        if self.head is None:
            self.head = Node(value)
            return
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        return

    def append(self, value):
        """ Append a value to the end of the list. """    
        # TODO: Write function to append here
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        # TODO: Write function to search here
        if self.head is None:
            return None
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        return None
    
    def remove(self, value):
        """ Remove first occurrence of value. """
        # TODO: Write function to remove here
        if self.head is None:
            return 
        node = self.head
        if node.value == value:
            self.head = node.next
            return
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next
        return
    
    def pop(self):
        """ Return the first node's value and remove it from the list. """
        # TODO: Write function to pop here
        node = self.head
        self.head = node.next
        return node.value
    
    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """
            
        # TODO: Write function to insert here   
        node = self.head
        if pos == 0:
            self.head = Node(value)
            self.head.next = node
            return
        count = 0
        while node.next:
            #print(count)
            if count == pos-1:
                oldNode = node.next
                node.next = Node(value)
                node.next.next = oldNode
                return
            node = node.next
            count = count + 1
        if pos > count:
            node.next = Node(value)
            
        return

linked_list = LinkedList()
linked_list.prepend(4)
linked_list.prepend(1)
linked_list.insert(5,0)
linked_list.insert(2,1) 
linked_list.insert(3,6) 

print(linked_list.to_list())