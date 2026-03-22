"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        # Code here
        
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next)
        
        head.next.next = head
        head.next = None
        
        return new_head
        
        