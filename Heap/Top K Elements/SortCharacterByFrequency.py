class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        heap = []

        for ch, count in freq.items():
            heapq.heappush(heap, (-count, ch))

        result = []

        while heap:
            count, ch = heapq.heappop(heap)
            result.append(ch * (-count))

        return "".join(result)