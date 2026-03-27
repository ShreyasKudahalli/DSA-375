# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        info = {}

        def dfs(node, parent, depth):
            if not node:
                return
            
            info[node.val] = (parent, depth)

            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)

        dfs(root, None, 0)

        px, dx = info[x]
        py, dy = info[y]

        return dx == dy and px != py