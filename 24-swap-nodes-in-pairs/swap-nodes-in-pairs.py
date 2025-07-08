# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=[]
        while head:
            c.append(head)
            head=head.next
        
        for i in range(0,len(c)-1,2):
            c[i],c[i+1]=c[i+1],c[i]
        a=ListNode()
        b=a
        for i in c:
            b.next=i
            b=b.next
        b.next=None
        return a.next   