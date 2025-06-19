class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        a=s[::-1]
        for i in range(len(s)-1):
            for j in range(i,i+2):
                b=s[i]+s[j]
                if b in a:
                    return True
        return False