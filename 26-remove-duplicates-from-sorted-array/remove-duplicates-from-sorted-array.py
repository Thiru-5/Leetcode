class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        b=sorted(nums)
        for i in b:
            a=nums.count(i)
            if a>1:
                b=i
                nums.remove(i)
