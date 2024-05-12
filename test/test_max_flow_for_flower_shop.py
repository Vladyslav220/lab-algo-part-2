import unittest
import os
from src.max_flow_for_flower_shop import max_flow

cur_path = os.path.dirname(__file__)

class TestMaxFlowForFlowerShop(unittest.TestCase):

    def test_max_flow(self):
        input_file = os.path.join(cur_path, '..', 'resources', 'roads.csv')
        result = max_flow(input_file)
        self.assertEqual(result, 20)

    def test_max_flow_multi_graph(self):
        input_file = os.path.join(cur_path, '..', 'resources', 'roads_null.csv')
        result = max_flow(input_file)
        self.assertEqual(result, 0)

    def test_max_flow_empty(self):
        input_file = os.path.join(cur_path, '..', 'resources', 'roads_empty.csv')
        result = max_flow(input_file)
        self.assertEqual(result, 0)

    def test_max_flow_all_weight_1(self):
        input_file = os.path.join(cur_path, '..', 'resources', 'roads_weight_1.csv')
        result = max_flow(input_file)
        self.assertEqual(result, 2)
