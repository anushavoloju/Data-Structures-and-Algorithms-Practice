# Loop detection in the given linked list (determine if the linkedlist is circular or not)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
    
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return



def iscircular(linked_list):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """
    
    # TODO: Write function to check if linked list is circular
    if linked_list.head == None:
        return True
    slownode = linked_list.head
    fastnode = linked_list.head
    while slownode is not None and fastnode is not None:
        if slownode == fastnode:
            return True
        else:
            slownode = slownode.next
            fastnode = fastnode.next.next
    return False


list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next: 
    node = node.next   
node.next = loop_start

small_loop = LinkedList([0])
small_loop.head.next = small_loop.head

#print(list_with_loop.to_list())

print(iscircular(list_with_loop))
print(iscircular(LinkedList([-4, 7, 2, 5, -1])))
print(iscircular(LinkedList([1])))
print(iscircular(small_loop))
print(iscircular(LinkedList([])))