# Flatten the nested linked list

# A class behaves like a data-type, just like an int, float or any other built-in ones. 
# User defined class
class Node:
    def __init__(self, value): # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
# User defined class
class LinkedList: 
    def __init__(self, head): # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head
    
    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''
    def append(self, value):
        
        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return
        
        # Create a temporary Node object
        node = self.head
        
        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next
        
        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)

        
    '''We will need this function to convert a LinkedList object into a Python list of integers'''
    def to_list(self):
        out = []          # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object
        
        while node:       # <-- Iterate untill we have nodes available
            out.append(int(str(node.value))) # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            node = node.next
        
        return out

def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    '''
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    '''
    if list1.head is None and list2.head is None:
        return None
    elif list1 is None:
        return list2
    elif list2 is None:
        return list1
    else:
        node1 = list1.head
        node2 = list2.head
        if node1.value < node2.value:
            mergedList = LinkedList(Node(node1.value))
        else:
            mergedList = LinkedList(Node(node2.value))
        list1items = list1.to_list()
        list2items = list2.to_list()
        mergedListItems = list1items + list2items
        mergedListItems.sort()
        mergedListItems.pop(0)
        for item in mergedListItems:
            mergedList.append(item)
        return mergedList


''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''
class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)
    def _flatten(self, node):
        # TODO: Implement this method to flatten the linked list in ascending sorted order.
        if node.next is None:
            return merge(node.value, None)
        else:
            return merge(node.value, self._flatten(node.next))


linked_list1 = LinkedList(Node(1)) 
linked_list1.append(3)
linked_list1.append(5)

linked_list2 = LinkedList(Node(2)) 
linked_list2.append(4)
linked_list2.append(6)

print(linked_list1.to_list())
print(linked_list2.to_list())
print(merge(linked_list1, linked_list2).to_list())

nested_linked_list = NestedLinkedList(Node(linked_list1))
nested_linked_list.append(linked_list2)
print(nested_linked_list.flatten().to_list())