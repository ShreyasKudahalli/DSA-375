'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        #code here
        if head is None:
            return None

        if x == 1:
            return head.next
        
        temp = head
        curpos = 1
        
        while temp.next and curpos < x - 1:
            temp = temp.next
            curpos += 1
        
        if temp.next:
            temp.next = temp.next.next
        
        return head
        
