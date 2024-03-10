import unittest
from src.max_tree_diameter import BinaryTree, diameter_of_bin_tree


class TestBinaryTreeDiameter(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree(1)
        self.tree.left = BinaryTree(3)
        self.tree.right = BinaryTree(2)
        self.tree.left.left = BinaryTree(7)
        self.tree.left.right = BinaryTree(4)
        self.tree.left.left.left = BinaryTree(8)
        self.tree.left.left.left.left = BinaryTree(9)
        self.tree.left.right.right = BinaryTree(5)
        self.tree.left.right.right.right = BinaryTree(6)

    def test_diameter_of_binary_tree(self):
        self.assertEqual(diameter_of_bin_tree(self.tree), 6)

    def test_diameter_of_empty_tree(self):
        empty_tree = BinaryTree(None)
        self.assertEqual(diameter_of_bin_tree(empty_tree), 0)


if __name__ == "__main__":
    unittest.main()
