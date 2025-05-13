class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a=len(nums)/3
        c=Counter(nums)
        b=[]
        for i in c:
            if c[i]>a:
                b.append(i)
        return (b)