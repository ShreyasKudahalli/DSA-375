# Tree Node
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    
    #Function to find the least absolute difference between any node
    #value of the BST and the given integer.
    def minDiff(self,root, K):
        # code here
        
        ans = float('inf')
        curr = root

        while curr:
            ans = min(ans, abs(curr.data - K))

            if K < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        return ans