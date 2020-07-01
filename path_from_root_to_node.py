# find the path from root to node in a tree
class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from queue import Queue
def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree 
    """
    index = 0
    length = len(arr)
    
    if length <= 0 or arr[0] == -1:
        return None

    root = BinaryTreeNode(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)
    
    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1
        
        if left_child is not None:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            queue.put(left_node)
        
        right_child = arr[index]
        index += 1
        
        if right_child is not None:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root

def path_from_root_to_node(root, data):
    """
    :param: root - root of binary tree
    :param: data - value (representing a node)
    from root to the data node
    """
    path = recurse_path_from_root_to_node(root, data)
    return list(reversed(path))

def recurse_path_from_root_to_node(node, data):
    #path.append(node.data)
    if node.data == data:
        return [data]
    else:
        if node.left is not None:
            #leftpath.append(node.left.data)
            left = recurse_path_from_root_to_node(node.left, data)
            if left is not None:
                left.append(node.data)
                return left

        if node.right is not None:
            #rightpath.append(node.right.data)
            right = recurse_path_from_root_to_node(node.right, data)
            if right is not None:
                right.append(node.data)
                return right
        return None


root = convert_arr_to_binary_tree([1, 2, 3, 4, 5, None, None, None, None, None, None])
print(path_from_root_to_node(root, 5))