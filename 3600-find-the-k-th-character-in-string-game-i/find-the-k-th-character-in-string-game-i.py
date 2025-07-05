class Solution:
    def kthCharacter(self, k: int) -> str:
        a="a"
        while len(a)<k:
            for i in a:
                if i=="z":
                    a+="a"
                else:
                    a+=chr(ord(i)+1)
        return (a[k-1])