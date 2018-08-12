def is_symmetric(tree):
    def check_symmetry(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data and 
                    check_symmetry(subtree_0.left, subtree_0.right and 
                    check_symmetry(subtree_1.right, subtree_1.left)))
        return False
    
    return not tree or check_symmetry(tree.left, tree.right)