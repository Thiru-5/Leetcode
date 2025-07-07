class Solution:
    def findLucky(self, arr: List[int]) -> int:
        b=set(arr)
        a=[]
        c=Counter(arr)
        for i in b:
            if i==c[i]:
                a.append(i)
        if a:
            return (a[-1])
        else:
            return (-1)