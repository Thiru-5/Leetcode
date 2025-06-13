class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        a=min(nums)
        b=max(nums)
        c=b-a
        d=2*k
        if c<d:
            return 0
        else:
            return c-d