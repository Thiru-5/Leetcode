class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        #Points
        c=set()
        for i in nums:
            a,b=i
            for j in range(a,b+1):
                c.add(j)
        return (len(c))