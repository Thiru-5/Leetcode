class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n=len(arr)
        b=n//20
        a=arr[b:n-b]
        return (sum(a)/len(a))