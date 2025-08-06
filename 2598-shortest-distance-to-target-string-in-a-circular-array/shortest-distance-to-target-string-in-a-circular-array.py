class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res=[]
        n=len(words)
        for i in range(len(words)):
            if words[i]==target:
                pos=(i-startIndex+n)%n
                res.append(pos)
                neg=(startIndex-i+n)%n
                res.append(neg)
        if len(res)==0:
            return -1
            

        
            
        return min(res)
