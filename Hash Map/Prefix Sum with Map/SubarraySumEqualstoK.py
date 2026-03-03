class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0 : 1}
        total = 0
        res = 0
        for x in nums:
            total += x
            y = total-k
            if y in count:
                res += count[y]
                
            count[total] = count.get(total, 0) + 1
        return res