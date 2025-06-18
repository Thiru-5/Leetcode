class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total=0
        for i in range(len(nums)):
            unique=set()
            for j in range(i,len(nums)):
                unique.add(nums[j])
                total+=len(unique)**2
        return total

       
            

        