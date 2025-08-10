class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        a=sentence.split()
        b=[]
        k={"a","e","i","o","u","A","E","I","O","U"}
        for i in range(len(a)):
            if a[i][0] in k:
                c=(a[i]+"m")+("a"*(i+2))
            else:
                c=(a[i][1:len(a[i])]+a[i][0]+"m")+("a"*(i+2))
            b.append(c)
        c=" ".join(b)
        return (c)