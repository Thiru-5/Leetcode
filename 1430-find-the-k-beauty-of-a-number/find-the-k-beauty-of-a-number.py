class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        a=str(num)
        b=0
        for i in range(len(a)-(k-1)):
            c=int(a[i:i+k])
            if c!=0 and num%c==0:
                b+=1
        return (b)