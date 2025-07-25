# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a=ListNode()
        b=a
        while list1 and list2:
            if list1.val<list2.val:
                b.next=list1
                list1=list1.next
            else:
                b.next=list2
                list2=list2.next
            b=b.next
        if list1:
            b.next=list1
        else:
            b.next=list2
        return a.next