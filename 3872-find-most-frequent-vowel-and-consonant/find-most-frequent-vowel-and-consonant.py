class Solution:
    def maxFreqSum(self, s: str) -> int:
        se=set(s)
        a="aeiou"
        v=0
        c=0
        for i in se:
            k=s.count(i)
            if i in a and k>v:
                v=k
            elif i not in a and k>c:
                c=k
        return (v+c)