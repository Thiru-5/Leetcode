class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a=1
        nums.sort()
        for i in nums:
            if a==i:
                a+=1
        return a