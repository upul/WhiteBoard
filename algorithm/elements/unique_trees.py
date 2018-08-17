from collections import namedtuple


class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


SubTreeInfo = namedtuple('SubTreeInfo', ('status', 'value', 'number'))


def num_unique_sub_trees(tree):
    if tree and tree.left is None and tree.right is None:
        return SubTreeInfo(True, tree.data, 0)

    left = num_unique_sub_trees(tree.left)
    right = num_unique_sub_trees(tree.right)

    if (not left.status) and (not right.status):
        return SubTreeInfo(False, tree.data, 0)

    left_right_root_eq_data = (left.value == right.value == tree.data)

    if left.status and right.status and left_right_root_eq_data:
        return SubTreeInfo(True, tree.data, left.number + right.number + 1)

    if left.status and right.status:
        return SubTreeInfo(False, tree.data, left.number + right.number)

    if left.status or right.status:
        return SubTreeInfo(False, tree.data,
                           left.number if left.status else right.number)


if __name__ == '__main__':
    l1 = TreeNode(1)
    l2 = TreeNode(1)

    l3 = TreeNode(1)
    l4 = TreeNode(1)

    ll1 = TreeNode(1, l1, l2)
    ll2 = TreeNode(1, l3, l4)

    root = TreeNode(1, ll1, ll2)
    print(num_unique_sub_trees(root))
