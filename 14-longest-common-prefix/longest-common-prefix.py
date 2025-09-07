class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=""
        strs.sort()
        t=strs[0]
        v=strs[-1]
        for i in range(len(t)):
            if t[i]==v[i]:
                a+=t[i]
            else:
                break
        return (a)