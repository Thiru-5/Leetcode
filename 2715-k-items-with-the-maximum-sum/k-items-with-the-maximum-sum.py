class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        a=[1]*numOnes+[0]*numZeros+[-1]*numNegOnes
        b=sum(a[:k])
        return b