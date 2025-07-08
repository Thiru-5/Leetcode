lists = [[1,4,5],[1,3,4],[2,6]]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        c=[]
        for i in lists:

            while i:
                c.append(i.val)
                i=i.next
        c.sort()

        a=ListNode()
        b=a
        for i in c:
            b.next=ListNode(i)
            b=b.next
        return a.next