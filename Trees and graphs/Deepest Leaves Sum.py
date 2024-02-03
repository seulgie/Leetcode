# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 0))
        max_depth = 0
        result = 0

        while q:
            now, depth = q.popleft()

            if now.left: q.append((now.left, depth+1))
            if now.right: q.append((now.right, depth+1))
            if depth > max_depth:
                max_depth = depth
                result = 0
            if depth == max_depth:
                result += now.val

        return result



        
