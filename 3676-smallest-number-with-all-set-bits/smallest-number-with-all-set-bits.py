class Solution:
    def smallestNumber(self, n: int) -> int:
        l=10000
        for i in range(n,l):
            num=bin(i)[2:]
            if set(num)=={"1"}:
                return i
         