class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        a=float("inf")
        for i in target:
            b=s.count(i)//target.count(i)
            if b<a:
                a=b
        return (a)
