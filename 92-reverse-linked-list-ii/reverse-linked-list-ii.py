# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        c=[]
        a=ListNode()
        b=a
        while head:
            c.append(head.val)
            head=head.next
        c[left-1:right]=c[left-1:right][::-1]
        for i in c:
            b.next=ListNode(i)
            b=b.next
        b.next=None
        return a.next