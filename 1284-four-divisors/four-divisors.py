class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            b = set()
            for j in range(1, int(i**0.5) + 1):
                if i % j == 0:
                    b.add(j)
                    b.add(i // j)
                if len(b) > 4:   
                    
                    break
            if len(b) == 4:
                a += sum(b)
        return a
