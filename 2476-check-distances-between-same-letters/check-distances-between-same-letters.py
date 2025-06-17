class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        a={}
        ans=[]
        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]]=i
            else:
                an=abs(i-a[s[i]])-1
                expect=distance[ord(s[i])-ord("a")]
                if an!=expect:
                    return False
        return True
          


        
        