import unittest
import os
from src.gas_supply_checker import find_unreachable_cities

cur_path = os.path.dirname(__file__)

class TestGasSupplyBetweenStorage(unittest.TestCase):
    def test_gas_supply_between_cities(self):
        input_path = os.path.join(cur_path, '..', 'resources', 'input_gas.txt')
        output_path = os.path.join(cur_path, '..', 'resources', 'output_gas.txt')
        find_unreachable_cities(input_path, output_path)
        with open(output_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[0].strip(), "lviv ['morshyn', 'dashava', 'lutsk']")

    def test_gas_supply_empty(self):
        input_path = os.path.join(cur_path, '..', 'resources', 'input_gas_empty.txt')
        output_path = os.path.join(cur_path, '..', 'resources', 'output_gas_empty.txt')
        find_unreachable_cities(input_path, output_path)
        with open(output_path, 'r', encoding='utf-8') as file:
            first_line = file.readline().strip()
        self.assertIn(first_line, ['', 'No cities specified in the input file.'])

    def test_gas_supply_to_all_cities(self):
        input_path = os.path.join(cur_path, '..', 'resources', 'input_gas_to_all.txt')
        output_path = os.path.join(cur_path, '..', 'resources', 'output_gas_to_all.txt')
        find_unreachable_cities(input_path, output_path)
        with open(output_path, 'r', encoding='utf-8') as file:
            first_line = file.readline().strip()
        self.assertEqual(first_line, '')

if __name__ == '__main__':
    unittest.main()
