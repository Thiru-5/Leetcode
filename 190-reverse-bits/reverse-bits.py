class Solution:
    def reverseBits(self, n: int) -> int:
        b=format(n,'032b')
        a=b[::-1]
        return (int(a,2))