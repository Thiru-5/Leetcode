class Solution:
    def removeDuplicates(self, s: str) -> str:
        sta=[]
        for i in s:
            if len(sta)==0 or sta[-1]!=i:
                sta.append(i)
            else:
                sta.pop()
        return "".join(sta)

        