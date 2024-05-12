import unittest
import os
from src.wchain import *

class TestWchainOutput(unittest.TestCase):

    cur_path = os.path.dirname(__file__)

    def test_wchain_output(self):
        file_path = os.path.join(self.cur_path, '..', 'resources', 'wchain.out')
        with open(file_path, 'r') as f:
            output_value = int(f.read().strip())
        expected_value = 6
        self.assertEqual(output_value, expected_value)

    def test_wchain_number_output(self):
        file_path = os.path.join(self.cur_path, '..', 'resources', 'wchain_number.out')
        with open(file_path, 'r') as f:
            output_value = int(f.read().strip())
        expected_value = 4
        self.assertEqual(output_value, expected_value)

    def test_wchain_null_output(self):
        file_path = os.path.join(self.cur_path, '..', 'resources', 'wchain_null.out')
        with open(file_path, 'r') as f:
            output_value = int(f.read().strip())
        expected_value = 0
        self.assertEqual(output_value, expected_value)
