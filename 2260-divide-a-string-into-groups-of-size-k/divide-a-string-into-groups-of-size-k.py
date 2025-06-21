class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        a=[]
        for i in range(0,len(s),k):
            a.append(s[i:i+k])
        b=len(a[-1])
        if b!=k:
            c=k-b
            a[-1]=a[-1]+(fill*c)
        return (a)