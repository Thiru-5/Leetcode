class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=[]
        b=0
        i=0
        while i<len(s):
            if a!=[] and s[i] in a:
                a.pop(0)
            else:
                a.append(s[i])
                i+=1
            b=max(len(a),b)
        return (b)