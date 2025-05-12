class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        k=0
        for i in nums:
            a=str(i)
            b=len(a)
            c=0
            d=""
            for j in a:
                if int(j)>c:
                    c=int(j)
            d+=str(c)*b
            k+=int(d)
        return (k)