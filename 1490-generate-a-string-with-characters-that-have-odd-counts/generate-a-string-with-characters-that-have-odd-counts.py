class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==0:
            return "v"*(n-1)+"t"
        else:
            return "v"*n
    
        