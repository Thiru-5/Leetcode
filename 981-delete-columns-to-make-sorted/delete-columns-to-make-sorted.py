class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        b=0
        for i in range(len(strs[0])):
            a=""
            for j in strs:
                a+=j[i]
            if a!="".join(sorted(a)):
                b+=1
        return (b)
