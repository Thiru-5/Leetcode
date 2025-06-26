class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        a=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if gcd(int(str(nums[i])[0]), int(str(nums[j])[-1]))==1:
                    a+=1
        return (a)