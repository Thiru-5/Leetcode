class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        a=re.sub(r'[^a-zA-Z]','',licensePlate).lower()
        k="Thiruselvam"
        for i in words:
                if all(i.count(j) >= a.count(j) for j in a):
                    if len(k)>len(i):
                        k=i
        return (k) 