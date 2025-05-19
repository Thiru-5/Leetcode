class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a=len(set(nums))
        if a==1:
            return "equilateral"
        elif a==2 :
            if nums[0]+nums[1]>nums[2]:
                return "isosceles"
            return "none"
        elif a==3 :
            if nums[0]+nums[1]>nums[2]:
                return "scalene"
            return "none"