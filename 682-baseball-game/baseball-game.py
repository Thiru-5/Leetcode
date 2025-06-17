class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=[]
        for i in operations:
            try:
                b=int(i)
                a.append(b)
            except:
                if i=="C":
                    a.pop()
                elif i=="D":
                    a.append(a[-1]*2)
                else:
                    a.append(a[-1]+a[-2])
        return (sum(a))