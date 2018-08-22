class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def search_bstree(tree, key):
    return tree \
           if not tree or tree.data == key else \
           search_bstree(tree.left, key) if key < tree.data else \
           search_bstree(tree.right, key)

if __name__ == '__main__':
    left = BstNode(10, BstNode(8), BstNode(15))
    right = BstNode(30, right=BstNode(45))
    tree = BstNode(20, left, right)

    result = search_bstree(tree, 250)
    print(result.data)
