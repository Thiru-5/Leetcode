# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=[]
        while head:
            c.append(head)
            head=head.next
            
        c.remove(c[-(n)])

        a=ListNode()
        b=a
        for i in c:
            b.next=i
            b=b.next
        b.next=None
        return a.next