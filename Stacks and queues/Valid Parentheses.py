class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs= {"(":")", "{":"}", "[":"]"}
        
        if len(s)%2 == 1: return False
        
        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                recent = stack.pop()
                if pairs[recent] != c:
                    return False
        
        return False if len(stack) != 0 else True
    
