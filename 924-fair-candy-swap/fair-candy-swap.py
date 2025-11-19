class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a=sum(aliceSizes)
        b=sum(bobSizes)
        c=(a-b)//2

        d=set(bobSizes)

        for i in aliceSizes:
            j=i-c
            if j in bobSizes:
                return [i,j]