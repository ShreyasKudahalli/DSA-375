# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        stack = []
        temp = head

        while temp:
            if not stack:
                stack.append(temp)
            else:
                while stack and stack[-1].val < temp.val:
                    stack.pop()
                stack.append(temp)
            temp = temp.next
        
        head = None

        while stack:
            node = stack.pop()
            node.next = head
            head = node
        return head