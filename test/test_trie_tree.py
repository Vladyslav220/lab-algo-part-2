import unittest
import os
from src.trie_tree import build_trie_from_input_file

cur_path = os.path.dirname(os.path.abspath(__file__))

class TestTrieTree(unittest.TestCase):

    def test_trie_tree_fill(self):
        input_file_path = os.path.join(cur_path, "../resources/input_trie.txt")
        result = build_trie_from_input_file(input_file_path)
        self.assertEqual(len(result.search_words_with_prefix('fer')), 2)

    def test_trie_tree_empty(self):
        input_file_path = os.path.join(cur_path, "../resources/input_trie_empty.txt")
        result = build_trie_from_input_file(input_file_path)
        self.assertEqual(len(result.search_words_with_prefix('')), 0)
