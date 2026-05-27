# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dp(node):
            if not node:
                return (0, 0)
            
            left_rob, left_skip = dp(node.left)
            right_rob, right_skip = dp(node.right)
            now = node.val + left_skip + right_skip
            
            skip = max(left_rob, left_skip) + max(right_rob, right_skip)
            
            return (now, skip)
        
        return max(dp(root))
            