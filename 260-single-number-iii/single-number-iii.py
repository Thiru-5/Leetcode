class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        b=[]
        for i in nums:
            a=nums.count(i)
            if a%2==1:
                b.append(i)
        return b