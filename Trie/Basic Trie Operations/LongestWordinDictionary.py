class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.end = True
        ans = ""
        def dfs(node, path):
            nonlocal ans
            word = "".join(path)
            if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                ans = word
            for ch in sorted(node.children):
                child = node.children[ch]
                if child.end:
                    path.append(ch)
                    dfs(child, path)
                    path.pop()

        dfs(root, [])
        return ans

