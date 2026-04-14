# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        def dfs(node):
            if not node:
                return 0 
            
            l = dfs(node.left)
            r = dfs(node.right)

            l = max(l, 0)
            r = max(r, 0)
            
            self.ans = max(self.ans,(node.val + l + r))
            return max(node.val + l, node.val + r)
        dfs(root)
        return self.ans
