class Trie:
    def __init__(self):
        self.children = {}
        self.word = False

    def add(self, word):
        root = self
        for char in word:
            if char not in root.children: root.children[char]=Trie()
            root = root.children[char]
        root.word=True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for s in strs:
            trie.add(s)

        prefix = []
        node = trie
        while node and len(node.children) == 1 and not node.word:
            for char in node.children:
                prefix.append(char)
                node = node.children[char]
                break
        return "".join(prefix)