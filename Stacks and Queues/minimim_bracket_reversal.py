# calculate number of reversals required to fix the brackets

class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

def minimum_bracket_reversals(input_string):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       input_string(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of breacket reversals needed
    """
    
    # TODO: Write function here

    stack = Stack()
    count = 0
    for c in input_string:
        if c == '{':
            stack.push(c)
        elif c == '}':
            if stack.top() == '{':
                stack.pop()
            else:
                stack.push(c)
    while stack.is_empty() != True:
        str1 = stack.pop()
        str2 = stack.pop()
        if str1 == '}' and str2 == '}':
            count += 1
        elif str1 == '{' and str2 == '}':
            count += 2
        elif str1 == '{' and str2 == '{':
            count += 1
    return count

print(minimum_bracket_reversals("}}{{"))