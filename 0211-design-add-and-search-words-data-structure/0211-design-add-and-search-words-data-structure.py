class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root=Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children: curr.children[ch]=Trie()
            curr = curr.children[ch]
        curr.isWord=True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root
            for j in range(i, len(word)):
                ch = word[j]
                if ch!=".":
                    if ch not in curr.children: return False
                    curr = curr.children[ch]
                else:
                    for child in curr.children.values():
                        if dfs(j+1, child): return True
                    return False
            return curr.isWord
        return dfs(0, self.root)
        



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)