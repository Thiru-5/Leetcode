class Solution:
    def hammingWeight(self, n: int) -> int:
        a=bin(n)[2:]
        b=str(a)
        c=0
        for i in b:
            if i=="1":
                c+=1
        return(c)