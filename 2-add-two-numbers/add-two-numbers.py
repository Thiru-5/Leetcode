l1 = [2,4,3]
l2 = [5,6,4]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        a=ListNode()
        b=a
        f=0
        while l1 or l2 or f:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            c=x+y+f
            if c>9:
                k=str(c)
                f=int(k[0])
                c=int(k[-1])
            else:
                f=0
            b.next=ListNode(c)
            if l1:l1=l1.next
            if l2:l2=l2.next
            b=b.next
        return a.next