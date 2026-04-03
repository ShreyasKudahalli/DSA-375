# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mpp = {}
        for i in range(len(inorder)):
            mpp[inorder[i]]=i

        def build(preorder,pstart,pend,inorder,istart,iend,mpp):

            if pstart > pend or istart > iend:
                return None

            root_val = preorder[pstart]
            root = TreeNode(root_val)

            inRoot = mpp[root_val]

            numsLeft = inRoot - istart

            root.left = build(
                preorder,
                pstart + 1,
                pstart + numsLeft,
                inorder,
                istart,
                inRoot - 1,
                mpp
            )

            root.right = build(
                preorder,
                pstart + numsLeft + 1,
                pend,
                inorder,
                inRoot + 1,
                iend,
                mpp
            )

            return root

        return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, mpp)
