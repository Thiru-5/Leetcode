class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        res=[]
        for i in range(n):
            ans=0
            if k>0:
                for j in range(1,k+1):
                    ans+=code[(i+j)%n]
                res.append(ans)
            elif k<0:
                for j in range(1,abs(k)+1):
                    ans+=code[(i-j)%n]
                res.append(ans)
            else:
                res.append(ans)

        return res
    