class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()

        for word in wordDict:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.end = True

        n = len(s)
        memo = {}

        def dfs(start):
            if start == n:
                return True

            if start in memo:
                return memo[start]

            node = root

            for i in range(start, n):
                ch = s[i]

                if ch not in node.children:
                    break

                node = node.children[ch]

                if node.end and dfs(i + 1):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return dfs(0)