# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
head = [1,1,2]
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=ListNode()
        b=a
        while head:
            c=head.val
            d=head.next.val if head.next else None
            if c!=d:
                b.next=head
                b=b.next
            head=head.next
        b.next=None
        return a.next