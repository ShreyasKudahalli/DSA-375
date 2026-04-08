class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, level = q.popleft()

            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + ch + word[i+1:]

                    if new_word == endWord:
                        return level + 1

                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        q.append((new_word, level + 1))

        return 0