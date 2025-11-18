class Solution:
    def reverse(self, x: int) -> int:
        a=str(x)
        b=a[::-1]
        try:
            a=(int(b))
        except:
            b=b.replace("-","")
            a=(-(int(b)))
        if a>2**31-1 or a<(-2**31):
            return 0
        return a