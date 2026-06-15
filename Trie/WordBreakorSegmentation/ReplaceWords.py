class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        root = TrieNode()

        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.end = True
        
        def findRoot(word):
            node = root
            prefix = ""
            for ch in word:
                if ch not in node.children:
                    return word
                else:
                    prefix += ch
                    node = node.children[ch]
                    if node.end:
                        return prefix
            return word

        words = sentence.split()

        for i in range(len(words)):
            words[i] = findRoot(words[i])

        return " ".join(words)