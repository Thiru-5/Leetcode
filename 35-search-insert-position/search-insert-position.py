class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        for i in range(len(nums)):
            if target < nums[i]:
                return i
        return len(nums)
