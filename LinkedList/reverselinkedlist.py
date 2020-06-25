# Reverse the given linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])

def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    revlist = LinkedList()
    items = [v for v in linked_list]
    revItems = []
    i = 0
    l = len(items)
    while i < l:
        revItems.append(items.pop())
        i = i + 1
    for ritem in revItems:
        revlist.append(ritem)
    
    # TODO: Write your function to reverse linked lists here
    
    return revlist

llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

#print(llist.__repr__())

flipped = reverse(llist)
print(flipped.__repr__())