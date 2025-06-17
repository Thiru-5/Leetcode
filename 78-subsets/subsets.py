class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[]
        for i in range(len(nums)+1):
            for j in combinations(nums,i):
                a.append(j)
        return a