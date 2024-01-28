class Solution:
    def simplifyPath(self, path: str) -> str:

        # Initialize a stack
        stack = []

        # Split the input string on "/" and process each part
        for part in path.split("/"):
            if part == ".." and len(stack) > 0:
                stack.pop()
            elif part != '.' and part != '..' and part !='':
                stack.append(part)

        return "/" + "/".join(stack)
