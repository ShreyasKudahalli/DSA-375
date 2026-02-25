#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def constructDLL(self, arr):
        # Code here
        head = None
        tail = head
        
        for x in arr:
            node = Node(x)
            
            if not head:
                head = node
                tail = head
            else:
                tail.next = node
                node.prev = tail
                tail = tail.next
        return head