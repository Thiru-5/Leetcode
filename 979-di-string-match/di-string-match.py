class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        a=0
        b=len(s)
        c=[]
        for i in s:
            if i=="I":
                c.append(a)
                a+=1
            else:
                c.append(b)
                b-=1
        if s[-1]=="I":
            c.append(a)
        elif s[-1]=="D":
            c.append(b)
        return c