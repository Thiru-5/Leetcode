class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        b=[]
        for i in ranges:
            b+=range(i[0],i[1]+1)
        for i in range(left,right+1):
            if i not in b:
                return False
        return True