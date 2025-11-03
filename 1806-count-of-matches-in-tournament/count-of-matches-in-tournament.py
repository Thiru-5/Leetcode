class Solution:
    def numberOfMatches(self, n: int) -> int:
        v=0
        while n!=1:
            if n%2==0:
                n=n//2
                v+=n
            if n%2==1:
                n=(n-1)//2+1
                v+=n-1
        return v