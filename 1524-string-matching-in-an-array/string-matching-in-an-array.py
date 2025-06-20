class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        a=set()
        for i in words:
            for j in words:
                if i!=j and i in j:
                    a.add(i)
                    break
        return list(a)