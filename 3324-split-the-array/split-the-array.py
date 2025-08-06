class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums.sort()
        a=[]
        b=[]
        for i in range(0,len(nums),2):
            if nums[i] in a or nums[i+1] in b:
                return False
            a.append(nums[i])
            b.append(nums[i+1])
        return True