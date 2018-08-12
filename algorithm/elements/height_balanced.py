
from collections import namedtuple


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balance(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)

        left_result = check_balance(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balance(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height)
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balance(tree).balanced


if __name__ == '__main__':
    L21 = BinaryTreeNode(271)
    L22 = BinaryTreeNode(561)

    L23 = BinaryTreeNode(2)
    L24 = BinaryTreeNode(271)

    L11 = BinaryTreeNode(6, L21, L22)
    L12 = BinaryTreeNode(6, L23, L24)

    root = BinaryTreeNode(314, L11, L12)

    print(is_balanced_binary_tree(root))
