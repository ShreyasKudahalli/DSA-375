# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        def reverse(head):
            prev = None
            cur = head
            temp = None

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        mid = slow.next
        slow.next = None

        right = reverse(mid)
        left = head

        while left and right:
            temp1 = left.next
            temp2 = right.next

            left.next = right
            right.next = temp1

            left = temp1
            right = temp2
        
        return head