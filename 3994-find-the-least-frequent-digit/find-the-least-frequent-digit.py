from collections import Counter 
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        a = []
        b = str(n)
        for i in b:
            if b.count(i) == min(b.count(x) for x in b):
                a.append(int(i))
        a.sort()
        return a[0]
