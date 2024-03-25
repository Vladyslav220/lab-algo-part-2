import unittest
from src.find_the_shortest_safe_route import *

class TestBFSShortMinesPath(unittest.TestCase):
    def test_normal_case(self):
        find_shortest_safe_route("input.txt", "output.txt")
        with open('output.txt', 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()

        self.assertEqual(int(numbers[0]), 12)

    def test_empty_input(self):
        find_shortest_safe_route("input_empty.txt", "output_empty.txt")
        with open('output_empty.txt', 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()
        self.assertEqual(int(numbers[0]), -1)
