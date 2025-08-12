class Solution:
    def largestGoodInteger(self, num: str) -> str:
        c=0
        b=""
        for i in range(len(num)):
            a=num[i:i+3]
            if a.count(num[i])==3:
                if  int(num[i])>=c:
                    c=int(num[i])
                    b=a
        return b
        