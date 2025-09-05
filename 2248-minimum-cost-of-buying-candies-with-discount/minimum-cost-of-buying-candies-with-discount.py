class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        a=0
        cost.sort(reverse=True)
        count=0
        for i in cost:
            if count<2:
                a+=i
                count+=1
            else:
                count=0
        return a

        
        