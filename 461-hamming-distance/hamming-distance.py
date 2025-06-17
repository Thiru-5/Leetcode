class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count=0
        length=max(x.bit_length(),y.bit_length())

        a=str(format(x,f'0{length}b'))
        b=str(format(y,f'0{length}b'))
        for i in range(length):
            if a[i]=="1" and b[i]=="0":
                count+=1
            elif a[i]=="0" and b[i]=="1":
                count+=1
        return count