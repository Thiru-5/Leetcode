# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        c=[]
        while head:
            c.append(head.val)
            head=head.next
        for i in range(len(c)-1):
            k=c[i+1:]
            for j in k:
                if c[i]<j:
                    c[i]=j
                    break
            else:
                c[i]=0
        c[-1]=0
        return (c)
