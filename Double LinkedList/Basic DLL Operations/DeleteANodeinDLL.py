"""
class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None
"""

class Solution:
    def delPos(self, head, x):
        if not head:
            return None
        
        temp = head
        count = 1
        
        if x == 1:
            head = head.next
            if head:
                head.prev = None
            return head
        
        while temp and count < x:
            temp = temp.next
            count += 1
        
        if not temp:
            return head
        
        if temp.next:
            temp.next.prev = temp.prev
        
        if temp.prev:
            temp.prev.next = temp.next
        
        return head