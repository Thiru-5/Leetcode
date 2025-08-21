class Solution:
    def alternateDigitSum(self, n: int) -> int:
        b=str(n)
        a=0
        for i in range(len(b)):
            if i%2==0:
                a+=int(b[i])
            else:
                a-=int(b[i])
        return a
        