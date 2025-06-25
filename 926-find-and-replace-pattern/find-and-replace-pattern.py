class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res=[]
        for i in words:
            s1={}
            s2={}
        
            match=True
            
            for sc,tc in zip(i,pattern):
                if sc in s1:
                    if s1[sc]!=tc:
                        match=False
                s1[sc]=tc
                if tc in s2:
                    if s2[tc]!=sc:
                        match=False
                s2[tc]=sc
            if match==True:
                res.append(i)
        return res




        