# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=ListNode()
        b=a
        c=[]
        while head:
            c.append(head.val)
            head=head.next
        k=c[::-1]
        for i in k:
            b.next=ListNode(i)
            b=b.next
        return a.next