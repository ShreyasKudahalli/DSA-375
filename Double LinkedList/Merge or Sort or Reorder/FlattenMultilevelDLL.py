"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        node = head

        while node:
            if node.child:
                temp = node.child
                while temp.next:
                    temp = temp.next
                temp.next = node.next
                
                if node.next:
                    node.next.prev = temp 
                node.next = node.child
                node.child.prev = node
                node.child = None
            node = node.next
        return head


