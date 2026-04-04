# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        temp = root
        
        while temp:
            if temp.val > val:
                if not temp.left:
                    temp.left = TreeNode(val)
                    return root
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = TreeNode(val)
                    return root
                temp = temp.right
        return root