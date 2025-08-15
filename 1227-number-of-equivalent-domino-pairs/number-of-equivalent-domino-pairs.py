class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        a = 0
        seen = {}
        for i in range(len(dominoes)):
            # sort each domino so [2,1] becomes [1,2]
            key = tuple(sorted(dominoes[i]))
            if key in seen:
                a += seen[key]
                seen[key] += 1
            else:
                seen[key] = 1
        return a
