class Solution:
    def romanToInt(self, s: str) -> int:
        a=[]
        b=[]
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for k in s:
            a.append(roman[k])
        i=0
        while i<len(a):
            if i<len(a)-1 and a[i]<a[i+1]:
                b.append(a[i+1]-a[i])
                i+=2
            else:
                b.append(a[i])
                i+=1
        return(sum(b))