class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a=haystack
        if needle in a:
            return(a.index(needle))
        return(-1)