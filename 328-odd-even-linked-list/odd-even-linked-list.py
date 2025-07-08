# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=ListNode()
        b=a

        c=ListNode()
        d=c
        i=1
        while head:
            if i%2==1:
                b.next=head
                b=b.next
            else:
                d.next=head 
                d=d.next
            head=head.next
            i+=1
        d.next=None
        b.next=c.next
        return a.next
