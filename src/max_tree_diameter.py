class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def diam_and_depth(node):
    if not node:
        return 0, 0

    left_diameter, left_depth = diam_and_depth(node.left)
    right_diameter, right_depth = diam_and_depth(node.right)
    current_depth = max(left_depth, right_depth) + 1
    current_diameter = max(left_depth + right_depth, left_diameter, right_diameter)

    return current_diameter, current_depth


def diameter_of_bin_tree(root):
    diameter = diam_and_depth(root)[0]
    return diameter

