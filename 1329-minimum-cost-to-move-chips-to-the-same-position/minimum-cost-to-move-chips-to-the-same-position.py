class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        a=0
        b=0
        for i in position:
            if i%2==0:
                a+=1
            else:
                b+=1
        return min(a,b)
            

        