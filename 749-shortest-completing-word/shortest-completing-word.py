class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        a=re.sub(r'[^a-zA-Z]','',licensePlate).lower()
        k=[]
        for i in words:
                if all(i.count(j) >= a.count(j) for j in a):
                        k.append(i)
        k.sort(key=len)
        return (k[0]) 