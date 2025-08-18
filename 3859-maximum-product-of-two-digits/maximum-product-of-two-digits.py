class Solution:
    def maxProduct(self, n: int) -> int:
        a=str(n)
        b=[]
        for i in a:
            b.append(int(i))
        b.sort(reverse=True)
        return b[0]*b[1]