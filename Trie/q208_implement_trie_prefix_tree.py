# Time:  O(n)
# Space: O(1)

# Ideas:
#
from collections import defaultdict


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        trie_tree = lambda: defaultdict(trie_tree)
        self.trie = trie_tree()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.trie
        for c in word:
            cur = cur[c]
        cur['#'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.trie
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '#' in cur

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.trie
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
