class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        a=0
        for i in items:
            if ruleKey=="type":
                if i[0]==ruleValue:
                    a+=1
            elif ruleKey=="color":
                if i[1]==ruleValue:
                    a+=1
            else:
                if i[2]==ruleValue:
                    a+=1
        return (a)