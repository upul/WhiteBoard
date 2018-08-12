def has_path_sum(tree, expected_sum, current_sum=0):
    if not tree:
        return False

    if not tree.left and not tree.right:
        return (current_sum + tree.data) == expected_sum

    return (has_path_sum(tree.left, expected_sum, current_sum + tree.data) or
            has_path_sum(tree.right, expected_sum, current_sum + tree.data))


def print_path_sum(tree, weight):
    def calculate_path_sum(ccr_node, current_weight):
        if not ccr_node:
            return []

        if not ccr_node.left and not ccr_node.right:
            if (current_weight + ccr_node.data) == weight:
                return [ccr_node.data]
            else:
                return []

        left = calculate_path_sum(
            ccr_node.left, current_weight + ccr_node.data)
        right = calculate_path_sum(
            ccr_node.right, current_weight + ccr_node.data)

        #left.append(ccr_node.data) if len(left) > 0 else left 
        #right.append(ccr_node.data) if len(right) > 0 else right
        if len(left) > 0:
            left.append(ccr_node.data)
        if len(right) > 0:
            right.append(ccr_node.data)

        return [ x for x in (left, right) if len(x) > 0]

    return calculate_path_sum(tree, current_weight=0)


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(3, n1)
    n3 = TreeNode(2)
    n4 = TreeNode(6, n3)
    n5 = TreeNode(2, n2, n4)
    n6 = TreeNode(1)
    n7 = TreeNode(2, n5, n6)

    #assert has_path_sum(n7, 8) == True
    #assert has_path_sum(n7, 120) == False
    #assert has_path_sum(n7, 3) == True

    print(print_path_sum(n7, 8))
