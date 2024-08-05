class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def delete(self, word: str) -> None:
        self._delete(self.root, word, 0)

    def _delete(self, node: TrieNode, word: str, depth: int) -> bool:
        if node is None:
            return False

        if depth == len(word):
            if not node.is_end_of_word:
                return False
            node.is_end_of_word = False
            return len(node.children) == 0

        char = word[depth]
        if char in node.children:
            should_delete_child = self._delete(node.children[char], word, depth + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0

        return False


# Example usage:
if __name__ == "__main__":
    trie = Trie()

    # Insert words
    trie.insert("hello")
    trie.insert("hell")
    trie.insert("he")

    # Search words
    print("Search 'hello':", trie.search("hello"))  # Output: True
    print("Search 'hell':", trie.search("hell"))  # Output: True
    print("Search 'he':", trie.search("he"))  # Output: True
    print("Search 'helloo':", trie.search("helloo"))  # Output: False

    # Delete a word
    trie.delete("hell")
    print("Search 'hell':", trie.search("hell"))  # Output: False
