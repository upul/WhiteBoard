class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def post_order(tree):
    if not tree:
        return []
    
    stack = []
    result = []
    stack.append(tree)
    
    while len(stack) > 0:
        current_node = stack.pop()
        result.append(current_node.data)

        if current_node.left:
            stack.append(current_node.left)

        if current_node.right:
            stack.append(current_node.right)

    assert len(stack) == 0

    result.reverse()
    return result

def pre_order(tree):
    if not tree:
        return []

    stack = []
    result = []
    stack.append(tree)

    while len(stack) > 0:
        current_node = stack.pop()
        result.append(current_node.data)

        if current_node.right:
            stack.append(current_node.right)

        if current_node.left:
            stack.append(current_node.left)
        
    assert len(stack) == 0   
     
    return result

def in_order(tree):
    result = []
    stack = []
    
    cct_node = tree
    while len(stack) > 0 or cct_node:
        if cct_node:
            stack.append(cct_node)
            cct_node = cct_node.left
        else:
            cct_node = stack.pop()
            result.append(cct_node.data)
            cct_node = cct_node.right
    return result

if __name__ == '__main__':
    L21 = BinaryTreeNode(271)
    L22 = BinaryTreeNode(561)

    L23 = BinaryTreeNode(2)
    L24 = BinaryTreeNode(271)

    L11 = BinaryTreeNode(6, L21, L22)
    L12 = BinaryTreeNode(60, L23, L24)

    root = BinaryTreeNode(314, L11, L12)

    print('post_order traversal')
    print(post_order(root))

    print('pre_order traversal')
    print(pre_order(root))

    print('In order traversal')
    print(in_order(root))
