# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def maxSum(root):
            nonlocal ans
            if root:
                left = max(0,maxSum(root.left))
                right = max(0,maxSum(root.right))
                ans = max(ans,left+right+root.val)
                return max(left,right)+root.val
            return 0
        maxSum(root)
        return ans