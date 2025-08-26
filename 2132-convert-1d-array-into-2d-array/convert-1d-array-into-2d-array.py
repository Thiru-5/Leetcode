class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            return []
        a=[]
        i=0
        for i in range(0,len(original),n):
            b=original[i:n+i]
            a.append(b)
        return a

            
