import unittest
from src.avl_priority_queue import Node, insert_into_queue, delete_from_queue, print_queue

class TestPriorityQueueMethods(unittest.TestCase):

    def test_insertion_and_deletion(self):
        # Create an empty queue
        root_node = None

        # Insertion
        root_node = insert_into_queue(root_node, 10, 6)
        root_node = insert_into_queue(root_node, 20, 5)
        root_node = insert_into_queue(root_node, 30, 3)
        root_node = insert_into_queue(root_node, 40, 2)
        root_node = insert_into_queue(root_node, 50, 1)
        root_node = insert_into_queue(root_node, 25, 4)

        root_node = delete_from_queue(root_node)

    def test_printing(self):
        # Create a sample tree
        root_node = Node(10, 6)
        root_node.left = Node(5, 5)
        root_node.right = Node(20, 8)

        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        print_queue(root_node)

        sys.stdout = sys.__stdout__

        printed_output = captured_output.getvalue().strip()

if __name__ == '__main__':
    unittest.main()
