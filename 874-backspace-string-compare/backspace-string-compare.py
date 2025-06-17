class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        c=[]
        d=[]
        for i in s:
            if i=="#":
                if c:
                    c.pop()
            else:
                c.append(i)

        for i in t:
            if i=="#":
                if d:
                    d.pop()
            else:
                d.append(i)

        return c==d