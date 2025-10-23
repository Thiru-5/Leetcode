from collections import Counter 
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        a = []
        b = str(n)
        k=min(b.count(x) for x in b)
        for i in b:
            if b.count(i) == k:
                a.append(int(i))
        a.sort()
        return a[0]
