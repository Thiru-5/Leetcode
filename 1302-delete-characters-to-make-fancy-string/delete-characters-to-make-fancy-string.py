class Solution:
    def makeFancyString(self, s: str) -> str:
        stack=[]        
        for ch in s:
            stack.append(ch)
            if len(stack) >= 3 and stack[-1] == stack[-2] == stack[-3]:
                stack.pop()  # remove one occurrence, turning xxx → xx

        s = "".join(stack)
        return (s)