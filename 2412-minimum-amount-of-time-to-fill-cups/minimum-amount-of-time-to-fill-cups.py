class Solution:
    def fillCups(self, amount: List[int]) -> int:
        if sum(amount)==0:
            return 0
        
        a=max(amount)

        return max(a,((sum(amount)+1)//2))
       

        