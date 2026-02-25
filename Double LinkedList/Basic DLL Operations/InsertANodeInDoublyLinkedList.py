'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def insertAtPos(self, head, p, x):
        node = Node(x)
        
        temp = head
        count = 0
        
        while temp and count < p:
            temp = temp.next
            count += 1
        
        if not temp:
            return head
        
        node.next = temp.next
        node.prev = temp
        
        if temp.next:
            temp.next.prev = node
        
        temp.next = node
        
        return head