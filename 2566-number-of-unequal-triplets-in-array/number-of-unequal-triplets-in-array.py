class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        a=0
        b=len(nums)
        for i in range(b):
            for j in range(i+1,b):
                for k in range(j+1,b):
                    if nums[i]!=nums[j] and nums[j]!=nums[k] and nums[i]!=nums[k]:
                        a+=1
        return (a)