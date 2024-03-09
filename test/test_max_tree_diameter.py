import unittest
from src.max_tree_diameter import BinaryTree, diameter_of_binary_tree


class TestBinaryTree(unittest.TestCase):
    def test_diameter_of_binary_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.right = BinaryTree(2)
        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)

        self.assertEqual(diameter_of_binary_tree(root), 6)

    def test_diameter_of_binary_tree_with_single_node(self):
        single_node = BinaryTree(5)
        self.assertEqual(diameter_of_binary_tree(single_node), 0)

if __name__ == '__main__':
    unittest.main()
