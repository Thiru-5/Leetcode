class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        a=b=0
        for i in nums:
            if i==0:
                a+=1
            elif a:
                b+=(a*(a+1))//2
                a=0
        b+=(a*(a+1))//2        
        return b

        