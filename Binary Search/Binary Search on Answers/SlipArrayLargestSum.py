class Solution:
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)

        def canSplit(maxSum):
            subarrays = 1
            currSum = 0

            for num in nums:
                if currSum + num > maxSum:
                    subarrays += 1
                    currSum = num
                else:
                    currSum += num

            return subarrays <= k

        while low <= high:
            mid = (low + high) // 2
            if canSplit(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low