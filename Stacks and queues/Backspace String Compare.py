class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for c in s:
            if stack1 and c == '#':
                stack1.pop()
            elif not stack1 and c == '#':
                stack1 = []
            else:
                stack1.append(c)

        for c in t:
            if stack2 and c == '#':
                stack2.pop()
            elif not stack2 and c == '#':
                stack2 = []
            else:
                stack2.append(c)

        return stack1 == stack2
