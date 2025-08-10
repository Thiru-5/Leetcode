class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        a=0
        b=0
        for i in costs:
            b+=i
            if b > coins:
                return a
            a+=1
        return a
        
            
