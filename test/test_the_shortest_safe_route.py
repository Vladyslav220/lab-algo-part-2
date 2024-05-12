import unittest
import os
from src.the_shortest_safe_route import find_shortest_safe_route

cur_path = os.path.dirname(__file__)

class TestBFSShortMinesPath(unittest.TestCase):
    def test_normal_case(self):
        input_file = os.path.join(cur_path, '..', 'resources', 'input.txt')
        output_file = os.path.join(cur_path, '..', 'resources', 'output.txt')
        find_shortest_safe_route(input_file, output_file)
        with open(output_file, 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()
        self.assertEqual(int(numbers[0]), 12)

    def test_empty_input(self):
        input_file = os.path.join(cur_path, '..', 'resources', 'input_empty.txt')
        output_file = os.path.join(cur_path, '..', 'resources', 'output_empty.txt')
        find_shortest_safe_route(input_file, output_file)
        with open(output_file, 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()
        self.assertEqual(int(numbers[0]), -1)
