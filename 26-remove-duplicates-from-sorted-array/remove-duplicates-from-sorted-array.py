class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums[:]:
            a=nums.count(i)
            if a>1:
                b=i
                nums.remove(i)
        