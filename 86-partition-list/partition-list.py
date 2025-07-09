# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        c=[]
        a=ListNode()
        b=a

        while head:
            if head.val<x:
                b.next=head
                b=b.next
            else:
                c.append(head)
            head=head.next

        for i in c:
            b.next=i
            b=b.next
        b.next=None
        return a.next