# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        Q = deque([root])

        while Q:
            n = len(Q)
            level = []

            for _ in range(n):
                node = Q.popleft()
                level.append(node.val)

                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            res.append(level)
        return res