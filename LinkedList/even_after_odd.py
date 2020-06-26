# Given a linked list, return all even elements after odd elements

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    evenlist = []
    oddlist = []
    while head:
          if head.data % 2 == 0:
              evenlist.append(head.data)
          else:
              oddlist.append(head.data)
          head = head.next
    
    newlist_head = create_linked_list(oddlist + evenlist)
    return newlist_head


head = create_linked_list([1, 2, 3, 4, 5, 6])
print_linked_list(head)
newhead = even_after_odd(head)
print_linked_list(newhead)