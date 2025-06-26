class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b=text.count("b")//1
        a=text.count("a")//1
        l=text.count("l")//2
        o=text.count("o")//2
        n=text.count("n")//1

        return (min(b,a,l,o,n))