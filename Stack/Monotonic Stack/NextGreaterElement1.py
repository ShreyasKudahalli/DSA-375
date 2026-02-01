class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mpp = {}
        n = len(nums2)
        stack = []

        for i in range(n-1,-1,-1):
            while stack and nums2[stack[-1]] <= nums2[i]:
                stack.pop()
            
            if stack:
                mpp[nums2[i]] = nums2[stack[-1]]
            else:
                mpp[nums2[i]] = -1
            stack.append(i)
        return [mpp[x] for x in nums1]