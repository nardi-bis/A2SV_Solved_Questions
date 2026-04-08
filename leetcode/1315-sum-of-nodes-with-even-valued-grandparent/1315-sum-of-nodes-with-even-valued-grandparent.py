# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def rec(node):
            # nonlocal ans
            ans = 0
            if not node:
                return 0
            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        ans += node.left.left.val
                    if node.left.right:
                        ans += node.left.right.val
                if node.right:
                    if node.right.right:
                        ans += node.right.right.val
                    if node.right.left:
                        ans += node.right.left.val

            ans += rec(node.left)
            ans += rec(node.right)
            return ans
        
        return rec(root)

                


        