class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp=-1
        for i in range(len(arr)-1,-1,-1):
            current=arr[i]
            arr[i]=temp
            temp=max(temp,current)
        return arr
            
          
        