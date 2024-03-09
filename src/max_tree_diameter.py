class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def max_depth(node):
    if not node:
        return 0
    else:
        left_depth = max_depth(node.left)
        right_depth = max_depth(node.right)
        return max(left_depth, right_depth) + 1

def diameter_of_binary_tree(root):
    if not root:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    left_diameter = diameter_of_binary_tree(root.left)
    right_diameter = diameter_of_binary_tree(root.right)
    return max(left_depth + right_depth, max(left_diameter, right_diameter))

root = BinaryTree(1)
root.left = BinaryTree(3)
root.right = BinaryTree(2)
root.left.left = BinaryTree(7)
root.left.right = BinaryTree(4)
root.left.left.left = BinaryTree(8)
root.left.left.left.left = BinaryTree(9)
root.left.right.right = BinaryTree(5)
root.left.right.right.right = BinaryTree(6)

print("Max tree diameter:", diameter_of_binary_tree(root))

