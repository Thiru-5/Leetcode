# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        c=[]
        while head:
            c.append(head)
            head=head.next
        k = k % len(c) if c else 0
        for i in range(k):
            c.insert(0,c.pop())
        if c:
            c[-1].next = None

        a=ListNode()
        b=a
        for i in c:
            b.next=i
            b=b.next
        return a.next