class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode()
        for word in strs:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.end = True

        ans = []
        node = root

        while len(node.children) == 1 and not node.end:
            ch = next(iter(node.children))
            ans.append(ch)
            node = node.children[ch]

        return "".join(ans)