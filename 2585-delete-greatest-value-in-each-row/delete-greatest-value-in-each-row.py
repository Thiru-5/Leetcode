class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        c=0
        for i in range(len(grid[0])):
            b=0
            for i in grid:
                a=max(i)
                i.remove(a)
                if a>b:
                    b=a
            c+=b
        return (c)