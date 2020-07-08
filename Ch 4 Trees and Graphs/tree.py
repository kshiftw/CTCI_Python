class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.array = []
        self.parent = None

    def get_children(self):
        def traverse(node):
            if not node:
                return
            self.array.append(node.value)
            traverse(node.left)
            traverse(node.right)
        traverse(self)
        return self.array