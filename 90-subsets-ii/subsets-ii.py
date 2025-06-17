class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a=set()
        for i in range(len(nums)+1):
            for j in combinations(nums,i):
                a.add(j)
        return list(a)