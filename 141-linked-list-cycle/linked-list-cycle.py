# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=set()
        while head:
            if head.next in a:
                return True
            a.add(head.next)
            head=head.next
        return False