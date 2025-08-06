class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        a=[]
        res=[]
        lenn=len(words)
        for i in words:
            a+=i
        b=set(a)
        return all( a.count(j)%len(words)==0 for j in b)


        