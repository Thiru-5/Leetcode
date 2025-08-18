class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        j=1
        a=nums[0][:]
        for i in nums[0]:
            for j in nums[1:] :
                if i not in j:
                    a.remove(i)
                    break
                    
        return(sorted(a))