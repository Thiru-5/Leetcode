# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=ListNode()
        b=a

        slow=head
        fast=head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        while head:
            if head!=slow:
                b.next=head
                b=b.next
            head=head.next
        b.next=None
        return a.next