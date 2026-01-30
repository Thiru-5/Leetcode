class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a=list(pattern)
        b=s.split()
        if len(a)!=len(b):
            return False
        else:
            return(len(set(zip(a,b)))==len(set(a))==len(set(b)))