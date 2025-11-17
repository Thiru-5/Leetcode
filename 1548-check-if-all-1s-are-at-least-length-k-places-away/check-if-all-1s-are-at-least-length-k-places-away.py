class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if nums[i]==1:
                a=nums[i+1:i+k+1]
                if 1 in a:
                    return (False)
        return (True)