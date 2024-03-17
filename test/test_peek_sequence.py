import unittest
from src.peek_sequence import peek_seq
class TestPeekSeq(unittest.TestCase):

    def test_sorted_ascending(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(peek_seq(arr), 0)

if __name__ == '__main__':
    unittest.main()
