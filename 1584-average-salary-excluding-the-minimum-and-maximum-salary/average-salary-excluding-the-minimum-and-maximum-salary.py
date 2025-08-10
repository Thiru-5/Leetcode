class Solution:
    def average(self, salary: List[int]) -> float:
        n=len(salary)
        a=sorted(salary)
        res=a[1:-1]
        summ=sum(res)
        return summ/len(res)