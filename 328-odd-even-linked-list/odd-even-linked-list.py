# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=[]
        while head:
            k=(head.val)
            c.append(k)
            head=head.next
        a=ListNode()
        b=a
        d=ListNode()
        f=d
        for i in range(len(c)):
            if i%2==0:
                b.next=ListNode(c[i])
                b=b.next
            else:
                f.next=ListNode(c[i])
                f=f.next
        f.next=None
        b.next=d.next
        return a.next