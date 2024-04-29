import unittest
import os
from src.max_flow_for_flower_shop import max_flow

cur_path = os.path.dirname(__file__)

class TestMaxFlowForFlowerShop(unittest.TestCase):

    def test_max_flow(self):
        result = max_flow('../resources/roads.csv')
        self.assertEqual(result, 20)

    def test_max_flow_multi_graph(self):
        result = max_flow('../resources/roads_null.csv')

        self.assertEqual(result, 0)

    def test_max_flow_empty(self):
        result = max_flow('../resources/roads_empty.csv')

        self.assertEqual(result, 0)

    def test_max_flow_all_weight_1(self):
        result = max_flow('../resources/roads_weight_1.csv')

        self.assertEqual(result, 2)
