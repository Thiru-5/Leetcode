class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans=[]
        for i in spells:
            mini=math.ceil(success/i)
            index = bisect_left(potions, mini)
            count=len(potions)-index
            ans.append(count)
        return ans

        
        