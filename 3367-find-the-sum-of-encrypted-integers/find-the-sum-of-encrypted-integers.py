class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        k=0
        for i in nums:
            a=max(str(i))
            b=len(str(i))
            c=(a*b)
            k+=int(c)
        return (k)