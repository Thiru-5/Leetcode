class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=Counter(nums)
        c = sorted(a.keys(), key=lambda x: a[x], reverse=True)
        return(c[:k])