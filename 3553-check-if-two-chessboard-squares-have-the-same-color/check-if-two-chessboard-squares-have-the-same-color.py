class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        a="aceg"
        k=0
        j=0
        if coordinate1[0] in a:
            k=1
        r=int(coordinate1[1])+k
        if coordinate2[0] in a:
            j=1
        p=int(coordinate2[1])+j


        if (r+p)%2==1:
            return False
        return True