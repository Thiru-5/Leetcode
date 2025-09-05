class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i=0
        a=""
        for j in spaces:
            a+=(s[i:j])
            a+=(" ")
            i=j
        a+=(s[i:])
        return a
        