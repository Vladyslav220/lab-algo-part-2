import unittest
from src.max_dist_between_cows import agr_cows

class TestAggressiveCows(unittest.TestCase):
    def test_example_1(self):
        N = 5
        C = 3
        free_sections = [1, 2, 8, 4, 9]
        self.assertEqual(agr_cows(N, C, free_sections), 3)

    def test_example_2(self):
        N = 5
        C = 2
        free_sections = [1, 2, 4, 8, 9]
        self.assertEqual(agr_cows(N, C, free_sections), 8)

    def test_example_3(self):
        N = 6
        C = 4
        free_sections = [1, 2, 3, 5, 6, 7]
        self.assertEqual(agr_cows(N, C, free_sections), 2)

    def test_example_4(self):
        N = 6
        C = 2
        free_sections = [1, 2, 3, 5, 6, 7]
        self.assertEqual(agr_cows(N, C, free_sections), 6)

if __name__ == '__main__':
    unittest.main()
