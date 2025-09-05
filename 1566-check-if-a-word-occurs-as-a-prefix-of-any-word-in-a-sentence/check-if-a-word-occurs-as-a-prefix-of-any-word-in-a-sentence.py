class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        a=sentence.split()
        b=len(searchWord)
        for i in a:
            if searchWord in i[0:b]:
                return ((a.index(i))+1)
        return -1