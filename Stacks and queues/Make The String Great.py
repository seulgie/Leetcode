class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if stack[-1].lower() != c.lower():
                    stack.append(c)
                elif stack[-1].isupper() != c.isupper():
                    stack.pop()
                else:
                    stack.append(c)
        
        return "".join(stack)
        
