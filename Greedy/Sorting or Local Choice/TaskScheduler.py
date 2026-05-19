class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        maxFreq = max(freq.values())

        maxCount = list(freq.values()).count(maxFreq)

        return max(
            len(tasks),
            (maxFreq - 1) * (n + 1) + maxCount
        )