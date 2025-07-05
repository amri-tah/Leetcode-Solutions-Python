class Trie():
    def __init__(self):
        self.children = {}
        self.products = []
    def insert(self, product):
        root = self
        for char in product:
            if char not in root.children: root.children[char] = Trie()
            root = root.children[char]  
            if len(root.products)<3: root.products.append(product)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        output = []
        products.sort()
        for product in products:
            root.insert(product)
        output = []
        node = root
        for char in searchWord:
            if node and char in node.children:
                node = node.children[char]
                output.append(node.products)
            else:
                node = None
                output.append([])

        return output
