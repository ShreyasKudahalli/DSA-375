# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return []
        
        stack = []
        temp = head
        res = []
        index = 0

        while temp:
            res.append(0)
            if not stack:
                stack.append((temp.val,index))
            else:
                while stack and stack[-1][0] < temp.val:
                    val,i = stack.pop()
                    res[i] = temp.val
                stack.append((temp.val,index))
            index += 1
            temp = temp.next
                
        return res
            