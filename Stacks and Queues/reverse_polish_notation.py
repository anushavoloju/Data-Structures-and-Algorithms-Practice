# Evaluate the given postfix expression and return the result integer value

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
    
    def to_list(self):
        out = []          # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object
        
        while node:       # <-- Iterate untill we have nodes available
            out.append(node.data) # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            node = node.next
        
        return out

def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """

    def is_integer(value: str, *, base: int=10) -> bool:
        try:
            int(value, base=base)
            return True
        except ValueError:
            return False

    stack = Stack()

    for item in input_list:
        if is_integer(item):
            stack.push(item)
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if item == '+':
                res = int(num1)+int(num2)
            elif item == '-':
                res = int(num1)-int(num2)
            elif item == '*':
                res = int(num1)*int(num2)
            if item == '/':
                res = int(int(num1)/int(num2))
            stack.push(res)
    
    result = stack.pop()
    
    return result

print(evaluate_post_fix(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))