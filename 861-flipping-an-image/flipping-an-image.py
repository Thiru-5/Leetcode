class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        c=[]
        for i in image:
            a=i[::-1]
            for j in range(len(a)):
                if a[j]==1:
                    a[j]=0
                else:
                    a[j]=1
            c.append(a)
        return (c)
