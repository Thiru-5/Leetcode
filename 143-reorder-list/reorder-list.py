# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        c=[]
        k=head
        j=k
        while k:
            c.append(k)
            k=k.next
        a=[]
        for i in range(len(c)//2):
            a.append(c[i])
            a.append(c[len(c)-i-1])
        if len(c) % 2 != 0:
            a.append(c[len(c) // 2])

        for i in range(len(a) - 1):
            a[i].next = a[i + 1]
        a[-1].next = None 
        