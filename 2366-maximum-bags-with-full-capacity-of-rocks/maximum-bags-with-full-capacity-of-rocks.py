class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        a=0
        b=[]
        for i in range(len(rocks)):
            b.append(capacity[i]-rocks[i])
        b.sort()
        for i in b:
            if i<=additionalRocks:
                a+=1
                additionalRocks-=i
        return a



        
