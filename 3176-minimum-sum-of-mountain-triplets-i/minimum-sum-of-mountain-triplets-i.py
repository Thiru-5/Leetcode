class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        b=100000
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]<nums[j] and nums[k]<nums[j]:
                        a=nums[i]+nums[j]+nums[k]
                        if a<b:
                            b=a
        if b==100000:
            return -1
        return b