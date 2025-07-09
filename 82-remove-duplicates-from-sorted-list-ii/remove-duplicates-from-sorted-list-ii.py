head = [1,2,3,3,4,4,5]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=ListNode()
        b=a
        c=[]
        while head:
                c.append(head.val)
                head=head.next
        
        for i in (c):
            if c.count(i)==1:
                b.next=ListNode(i)
                b=b.next
        b.next=None
        return a.next