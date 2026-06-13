class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestion = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = TrieNode()
        for product in products:
            node = root
            for ch in product:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                if len(node.suggestion) < 3:
                    node.suggestion.append(product)

        ans = []
        node = root

        for ch in searchWord:
            if node and ch in node.children:
                node = node.children[ch]
                ans.append(node.suggestion)
            else:
                node = None
                ans.append([])

        return ans
