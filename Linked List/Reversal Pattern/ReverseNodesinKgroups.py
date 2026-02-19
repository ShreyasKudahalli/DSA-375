# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head

        def kthnode(temp,k):
            n = k-1
            cur = temp
            while n and cur:
                cur = cur.next
                n -= 1
            return cur 

        while temp:
            knode = kthnode(temp,k)
            if knode == None:
                prev.next = None
                return head
            else:
                nextnode = knode.next
                knode.next = None
                new = reverse(temp)
                if temp == head:
                    head = new
                else:
                    prev.next = new
                prev = temp
                temp = nextnode
        return head