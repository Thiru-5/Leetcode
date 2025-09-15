class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a="aceg"
        k=0
        if coordinates[0] in a:
            k=1
        r=int(coordinates[1])+k
        if r%2==0:
            return False
        return True