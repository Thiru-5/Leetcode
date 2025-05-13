class Solution:
    def similarPairs(self, words: List[str]) -> int:
        c=0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if set(list(words[i]))==set(list(words[j])):
                    c+=1
        return (c)