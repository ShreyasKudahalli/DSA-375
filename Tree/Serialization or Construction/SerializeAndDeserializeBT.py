# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        q = deque([root])
        data = []

        while q:
            node = q.popleft()
            if node:
                data.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                data.append('#')

        return ','.join(data)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None

        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = deque([root])

        i = 1
        while q:
            node = q.popleft()
            if nodes[i] != '#':
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1
            if nodes[i] != '#':
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1

        return root
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))