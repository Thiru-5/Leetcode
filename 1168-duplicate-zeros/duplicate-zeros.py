class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        a=len(arr)
        res=[]
        i=0
        while i<a:
            if arr[i]==0:
                arr.insert(i,0)
                i+=2
            else:
                i+=1
        arr[:]=arr[:a]
