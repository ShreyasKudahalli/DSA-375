# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        count = 1
        res = []
        
        def rev(arr):
            l=0
            r=len(arr)-1
            while(l<r):
                arr[l],arr[r] = arr[r],arr[l]
                l += 1
                r -= 1
            return arr

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not count % 2:
                level = rev(level)
            count += 1
            res.append(level)
        
        return res