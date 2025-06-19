class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        a=0
        b=sorted(nums)
        if b==nums:
            return 0
        for i in nums[:]:
            nums.insert(0,nums.pop())
            a+=1
            if nums==b:
                return(a)
        return -1