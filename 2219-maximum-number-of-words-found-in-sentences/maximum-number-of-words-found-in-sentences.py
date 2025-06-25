class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        a=0
        for i in sentences:
            b=i.split()
            c=len(b)
            if c>a:
                a=c
        return (a)