class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        a=set()
        for i in words:
            for j in words:
                if i in j and i!=j:
                    a.add(i)
        return list(a)