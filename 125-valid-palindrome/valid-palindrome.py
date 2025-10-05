class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace("_","")
        a=re.sub(r'[^\w]','',s).lower()
        return (a==a[::-1])