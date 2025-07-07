# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        a=ListNode()
        b=a
        while head:
            if head.val!=val:
                b.next=head
                b=b.next
            head=head.next
        b.next=None
        return a.next