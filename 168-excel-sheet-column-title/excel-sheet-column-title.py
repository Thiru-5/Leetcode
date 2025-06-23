class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result=""
        while columnNumber>0:
            columnNumber-=1
            ans=columnNumber%26
            s=chr(ord("A")+ans)
            result=s+result
            columnNumber//=26
        return result
        
       

        