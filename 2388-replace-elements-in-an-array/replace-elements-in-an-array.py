class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indexmap={num:i  for i,num in enumerate(nums)}
        for old,new in operations:
            idx=indexmap[old]
            nums[idx]=new
            indexmap[new]=idx
            del indexmap[old]
        return nums


    

            
        