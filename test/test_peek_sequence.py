import unittest
from src.peek_sequence import peek_seq
class TestPeekSeq(unittest.TestCase):

    def test_sorted_ascending(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(peek_seq(arr), 0)

    def test_sorted_descending(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(peek_seq(arr), 0)

    def test_two_elements(self):
        arr = [1, 2]
        self.assertEqual(peek_seq(arr), 0)

    def test_no_peak_subsequences(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(peek_seq(arr), 0)

    def test_three_peak_subsequences(self):
        arr = [1, 3, 1, 5, 1, 4, 1]
        self.assertEqual(peek_seq(arr), 3)

if __name__ == '__main__':
    unittest.main()
