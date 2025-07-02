class Solution:
    def possibleStringCount(self, word: str) -> int:
        b=1
        for i in range(len(word)-1):
            if word[i]==word[i+1]:
                b+=1
        return (b)