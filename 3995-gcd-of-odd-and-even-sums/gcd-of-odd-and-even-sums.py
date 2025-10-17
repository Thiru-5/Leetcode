class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        a=0
        b=0
        for i in range(1,n+n+1):
            if i%2==0:
                a+=i
            else:
                b+=i
        return gcd(a,b)