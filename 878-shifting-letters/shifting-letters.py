class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        sa=list(s)
        a=0
        for i in reversed(range(len(s))):
            a=(a+shifts[i])%26
            b=chr((ord(sa[i]) - ord('a') + a) % 26 + ord('a'))
            sa[i]=b

        return "".join(sa)

        