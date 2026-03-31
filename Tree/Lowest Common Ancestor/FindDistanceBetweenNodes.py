# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def dfs(root,par):
            if root:
                parent[root]=par
                dfs(root.left,root)
                dfs(root.right,root)

        dfs(root,None)
        q = deque([target])
        visited = set([target])
        dist = 0

        while q:
            if dist == k:
                return [node.val for node in q]

            for _ in range(len(q)):
                node = q.popleft()
                for x in (node.left,node.right,parent[node]):
                    if x and x not in visited:
                        visited.add(x)
                        q.append(x)
            dist += 1
        return []