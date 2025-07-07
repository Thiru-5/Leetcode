class Solution:
    def findLucky(self, arr: List[int]) -> int:
        b=set(arr)
        a=[]
        for i in b:
            c=arr.count(i)
            if i==c:
                a.append(i)
        if a:
            return (a[-1])
        else:
            return (-1)