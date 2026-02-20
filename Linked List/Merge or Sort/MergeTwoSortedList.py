# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        head = None
        temp = None
        while list1 and list2:
            if list1.val >= list2.val:
                if head == None:
                    head = list2
                    temp = head
                else:
                    temp.next = list2
                    temp = temp.next
                list2 = list2.next
            else:
                if head == None:
                    head = list1
                    temp = head
                else:
                    temp.next = list1
                    temp = temp.next
                list1 = list1.next
        if list2:
            temp.next = list2
        else:
            temp.next = list1
        return head

