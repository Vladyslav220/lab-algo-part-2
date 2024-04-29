class TrieNode:
    def __init__(self, is_key=False, data=''):
        self.is_key = is_key
        self.data = data
        self.child = {}


class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.child:
                current.child[letter] = TrieNode(data=current.data + letter)
            current = current.child[letter]
        current.is_key = True

    def find(self, word):
        current = self.root
        for letter in word:
            if letter not in current.child:
                return None
            current = current.child[letter]
        if current.is_key:
            return current
        else:
            return None

    def delete(self, word):
        searched_node = self.find(word)
        if searched_node and searched_node.is_key:
            searched_node.is_key = False
            return searched_node.data
        else:
            return ''

    def __collect_words_recursively(self, current, words):
        if current.is_key:
            words.append(current.data)

        for child_node in current.child.values():
            self.__collect_words_recursively(child_node, words)

    def search_words_with_prefix(self, pref):
        current = self.root
        words = []
        for letter in pref:
            if letter not in current.child:
                return []
            current = current.child[letter]
        self.__collect_words_recursively(current, words)
        return words


def build_trie_from_input_file(file_read):
    pattern_list = read_file(file_read)
    trie_tree = TrieTree()
    for line in pattern_list:
        for word in line:
            trie_tree.insert(word)
    return trie_tree


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        return [line.strip().split() for line in lines] if lines else []
