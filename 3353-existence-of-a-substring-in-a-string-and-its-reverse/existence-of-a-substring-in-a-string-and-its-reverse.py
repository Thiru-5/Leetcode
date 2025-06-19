class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        a=s[::-1]
        for i in range(len(s)-1):
            b=s[i:i+2]
            if b in a:
                return True
        return False