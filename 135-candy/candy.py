class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        n=len(ratings)
        a=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                a[i]=a[i-1]+1

        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                a[i]=max(a[i],a[i+1]+1)
        return sum(a)