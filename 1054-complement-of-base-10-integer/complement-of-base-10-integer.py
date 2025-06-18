class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a=bin(n)[2:]
        b=""
        for i in a:
            if i=="0":
                b+="1"
            else:
                b+="0"
        return (int(b,2))