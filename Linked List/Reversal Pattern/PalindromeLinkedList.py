# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        cur = slow
        temp = slow
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        right = prev
        left = head

        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True