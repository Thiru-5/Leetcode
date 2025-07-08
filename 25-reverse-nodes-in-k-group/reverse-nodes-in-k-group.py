# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        c=[]
        while head:
            c.append(head)
            head=head.next
        
        d=[]
        for i in range(0,len(c),k):
            e=c[i:i+k]
            if len(e)==k:
                d+=e[::-1]
            else:
                d+=e
        a=ListNode()
        b=a
        for i in d:
            b.next=i
            b=b.next
        b.next=None
        return a.next            