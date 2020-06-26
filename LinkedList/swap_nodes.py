# Write a function to swap nodes present at position_one and position_two in given linked list. Do not create a new linked list

class Node:
    """LinkedListNode class"""
    def __init__(self, data):
        self.data = data
        self.next = None

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
        print(head.data, end=" ")
        head = head.next
    print()

"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped
"""
def swap_nodes(head, left_index, right_index):
    index = 0
    prev_left = None
    left = None
    prev_right = None
    right = None
    node = head

    while node is not None:
        if index == left_index - 1:
            prev_left = node
        if index == left_index:
            left = node
        if index == right_index - 1:
            prev_right = node
        if index == right_index:
            right = node
        index = index + 1
        node = node.next

    prev_right.next = left
    temp = left.next
    left.next = right.next
    if prev_left is not None:
        prev_left.next = right
    else:
        head = right
    right.next = temp

    return head

head = create_linked_list([3, 4, 5, 2, 6, 1, 9])
print_linked_list(head)
newhead = swap_nodes(head, 0, 1)
print_linked_list(newhead)