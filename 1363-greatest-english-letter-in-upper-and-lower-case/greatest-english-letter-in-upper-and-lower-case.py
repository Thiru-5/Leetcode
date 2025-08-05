class Solution:
    def greatestLetter(self, s: str) -> str:
        a=[]
        b=set(s)
        for i in b:
            if i.lower() in b and i.upper() in b:
                a.append(i.upper())
        c=sorted(a)
        if c:
            return c[-1]
        return ""
