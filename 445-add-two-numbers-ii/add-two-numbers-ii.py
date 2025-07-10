# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=[]
        d=[]
        while l1 or l2:
            if l1:
                c.append(l1.val)
            if l2:
                d.append(l2.val)
            if l1:l1=l1.next
            if l2:l2=l2.next
        e=int("".join(map(str,c)))
        f=int("".join(map(str,d)))
        g=str(int(e)+int(f))
        a=ListNode()
        b=a
        for i in g:
            b.next=ListNode(int(i))
            b=b.next
        b.next=None
        return a.next
