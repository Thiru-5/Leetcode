class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        b=len(nums)
        a=0
        for i in range(b):
            for j in range(i+1,b):
                for k in range(j+1,b):  
                    for l in range(k+1,b):
                        if nums[i]+nums[j]+nums[k]==nums[l]:
                            a+=1
        return a

        