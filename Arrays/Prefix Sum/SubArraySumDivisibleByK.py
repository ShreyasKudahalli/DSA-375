class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0 : 1}
        total = 0
        res = 0
        for x in nums:
            total += x
            y = total%k
            if y in count:
                res += count[y]
                count[y] += 1
            else:
                count[y] = 1
        return res