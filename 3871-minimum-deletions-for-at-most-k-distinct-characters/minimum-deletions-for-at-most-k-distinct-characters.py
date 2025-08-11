class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        a=Counter(s)
        distinct=len(a)
        dell=0
        ans=sorted(a.values())
        if distinct<=k:
            return 0
        anss=distinct-k
        for i in range(anss):
            dell+=ans[i]
        return dell