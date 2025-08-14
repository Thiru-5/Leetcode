class Solution:
    def clearDigits(self, s: str) -> str:

        sta=[]
        for i in s:
            if i.isdigit():
                sta.pop()
            else:
                sta.append(i)
        return "".join(sta)
        