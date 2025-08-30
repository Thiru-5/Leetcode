class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        dif=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                dif.append(i)
        if len(dif)==0:
            return True
        elif len(dif)==2:
            i,j=dif
            return s1[i]==s2[j] and s2[i]==s1[j]
        return False
       
            