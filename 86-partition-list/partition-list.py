# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a=ListNode()
        b=a
        c=ListNode()
        d=c
        while head:
            if head.val<x:
                b.next=head
                b=b.next
            else:
                d.next=head
                d=d.next
            head=head.next
        d.next=None
        b.next=c.next
        
        return a.next