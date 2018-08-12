class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def binary_tree_depth_order(tree):
    result = []
    if not tree:
        return result

    current_depth_nodes = [tree]
    while current_depth_nodes:
        result.append([node.data for node in current_depth_nodes])
        current_depth_nodes = [
            child
            for curr in current_depth_nodes for child in (curr.left, curr.right)
            if child
        ]
    return result

def binary_tree_bottom_up(root):
    result = []
    if not root:
        return result

    current_depth_nodes = [root]
    while current_depth_nodes:
        result.append([curr.data for curr in current_depth_nodes])
        current_depth_nodes = [
            child 
            for curr in current_depth_nodes for child in (curr.left, curr.right)
            if child
        ]
    result.reverse()
    return result
    
if __name__ == '__main__':
    L21 = BinaryTreeNode(271)
    L22 = BinaryTreeNode(561)

    L23 = BinaryTreeNode(2)
    L24 = BinaryTreeNode(271)

    L11 = BinaryTreeNode(6, L21, L22)
    L12 = BinaryTreeNode(6, L23, L24)

    root = BinaryTreeNode(314, L11, L12)

    print(binary_tree_bottom_up(root))
