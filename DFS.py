# Different ways of DFS traversal in a tree

class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

# define a stack to help keep track of the tree nodes
class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"

class State(object):
    def __init__(self,node):
        self.node = node
        self.visited_left = False
        self.visited_right = False
        
    def get_node(self):
        return self.node
    
    def get_visited_left(self):
        return self.visited_left
    
    def get_visited_right(self):
        return self.visited_right
    
    def set_visited_left(self):
        self.visited_left = True
        
    def set_visited_right(self):
        self.visited_right = True
        
    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
        return s

def pre_order(tree):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    pre_order_traversal(node, visit_order, stack, state)
    return visit_order

def pre_order_traversal(node, visit_order, stack, state):
    if node is not None:
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)
            pre_order_traversal(node, visit_order, stack, state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)
            pre_order_traversal(node, visit_order, stack, state)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
                pre_order_traversal(node, visit_order, stack, state)
            else:
                node = None
                pre_order_traversal(node, visit_order, stack, state)


def pre_order_recursion(tree):
    visit_order = list()
    root = tree.get_root()
    traverse(root, visit_order)

    return visit_order

def traverse(node, visit_order):
    if node is not None:
        #visit node
        visit_order.append(node.get_value())

        #traverse left
        traverse(node.get_left_child(), visit_order)

        #traverse right
        traverse(node.get_right_child(), visit_order)
    else:
        return


def in_order_recursion(tree):
    visit_order = list()
    root = tree.get_root()
    inorder_traverse(root, visit_order)

    return visit_order

def inorder_traverse(node, visit_order):
    if node is not None:
        inorder_traverse(node.get_left_child(), visit_order)
        visit_order.append(node.get_value())
        inorder_traverse(node.get_right_child(), visit_order)
    else:
        return


def post_order_recursion(tree):
    visit_order = list()
    root = tree.get_root()
    postorder_traverse(root, visit_order)

    return visit_order

def postorder_traverse(node, visit_order):
    if node is not None:
        postorder_traverse(node.get_left_child(), visit_order)
        postorder_traverse(node.get_right_child(), visit_order)
        visit_order.append(node.get_value())
    else:
        return

# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

print(pre_order(tree))

print(pre_order_recursion(tree))

print(in_order_recursion(tree))

print(post_order_recursion(tree))