class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res=[]
        c=0
        for i in nums:
            if i==0:
                c+=1
            else:
                a=c
                b=a*(a+1)//2
                res.append(b)
                c=0
        a=c
        b=a*(a+1)//2
        res.append(b)
        
        return sum(res)

        