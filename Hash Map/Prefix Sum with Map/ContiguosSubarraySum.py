class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_index = {0 : -1}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            rem = total % k
            if rem in rem_index:
                if i - rem_index[rem] >= 2:
                    return True
            else:
                rem_index[rem] = i
        return False
