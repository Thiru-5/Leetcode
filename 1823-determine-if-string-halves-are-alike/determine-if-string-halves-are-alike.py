class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l=len(s)//2
        a=s[:l]
        b=s[l:]
        v="aeiouAEIOU"
        c=0
        d=0
        for i in a:
            if i in v:
                c+=1
        for i in b:
            if i in v:
                d+=1
                
        return (c==d)