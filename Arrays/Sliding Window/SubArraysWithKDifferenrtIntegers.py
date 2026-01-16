class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        count = collections.defaultdict(int)
        l1,l2,r = 0,0,0
        res = 0

        while r < len(nums):
            count[nums[r]] += 1
            while len(count) > k:
                count[nums[l2]] -= 1
                if not count[nums[l2]]:
                    count.pop(nums[l2])
                l2 += 1
                l1 = l2
            while count[nums[l2]] > 1:
                count[nums[l2]] -= 1
                l2 += 1
        
            if len(count) == k:
                res += l2-l1+1
            
            r += 1
        return res