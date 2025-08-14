class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        sta=[]
        ans=[]
        for i in s:
            if sta and sta[-1][0]==i:
                sta[-1][1]+=1

                
                if sta[-1][1]==k:
                    sta.pop()
            else:
                sta.append([i,1])
        print(sta)
    
        for i in sta:
            ans.append(i[0]*i[1])
        return "".join(ans)
      
        




        