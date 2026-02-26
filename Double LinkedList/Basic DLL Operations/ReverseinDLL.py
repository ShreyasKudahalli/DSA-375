"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        if not head:
            return None
        
        temp = None
        current = head
        
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            
            current = current.prev
        
        if temp:
            head = temp.prev
        
        return head