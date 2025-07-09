# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=[]
        while head:
            c.append(head.val)
            head=head.next
        c.sort()
        a=ListNode()
        b=a
        for i in c:
            b.next=ListNode(i)
            b=b.next
        b.next=None
        return a.next