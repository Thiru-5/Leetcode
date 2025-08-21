class Solution:
    def minimumSum(self, num: int) -> int:
        a=str(num)
        b=sorted(a)
        i=0
        j=1
        c=int(b[0]+b[2])
        d=int(b[1]+b[3])
        return (c+d)