# Given a LinkedList head and i, j. skip first i nodes and delete next j nodes. 

class Node:
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
        print(head.data, end=' ')
        head = head.next
    print()

def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    ival = 0
    jval = 0
    itemList = []
    while head:
        itemList.append(head.data)
        head = head.next
    finalList = []
    itr = 0
    while itr < len(itemList):
        if ival <= i:
            if ival == i:
                ival = ival + 1
                jval = 0
            else:
                print("ival",ival)
                finalList.append(itemList[itr])
                ival = ival + 1
                itr = itr + 1
        elif jval <= j:
            if jval == j:
                jval = jval + 1
                ival = 0
            else:
                print("jval",jval)
                jval = jval + 1
                itr = itr + 1
        
        #itr = itr + 1
    new_head = create_linked_list(finalList)
    return new_head

head = create_linked_list([1,2,3,4,5])
print_linked_list(head)
newhead = skip_i_delete_j(head, 2, 1)
print_linked_list(newhead)