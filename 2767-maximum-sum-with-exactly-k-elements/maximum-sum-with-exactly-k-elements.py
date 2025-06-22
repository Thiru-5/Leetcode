class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        b=max(nums)
        a=0
        for i in range(k):
            a+=(b)
            b+=1
        return (a)