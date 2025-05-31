class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=prices[0]
        a=[]
        for j in range(1,len(prices)):
            if i > prices[j]:
                i = prices[j]
            else:
                a.append(prices[j]-i)
        return (max(a) if len(a)>0 else 0)