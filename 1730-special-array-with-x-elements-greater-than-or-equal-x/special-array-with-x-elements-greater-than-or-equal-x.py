class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n + 1):  
            a = sum(1 for j in nums if j >= i)
            if a == i:
                return i
        return -1
