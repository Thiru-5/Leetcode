# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        a=0
        nums = set(nums)
        while head:
            if (head.val in nums) and (not head.next or head.next.val not in nums):
                a+=1
            head=head.next
        return a