# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def rec(node):
            nonlocal ans
            if not node:
                return 
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

            rec(node.left)
            rec(node.right)
            return
        rec(root)
        return ans

                


        