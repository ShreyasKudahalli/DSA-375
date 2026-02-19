# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        tail = head
        length = 1
        
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        
        tail.next = head

        steps_to_new_tail = length - k
        temp = head
        
        for _ in range(steps_to_new_tail - 1):
            temp = temp.next
        new_head = temp.next
        temp.next = None
        
        return new_head