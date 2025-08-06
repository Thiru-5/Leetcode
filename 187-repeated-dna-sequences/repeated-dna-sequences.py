class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        c = set()
        d = set()

        for i in range(len(s) - 9):
            b = s[i:i+10]
            if b in c:
                d.add(b)
            else:
                c.add(b)

        a = list(d)
        return(a)
