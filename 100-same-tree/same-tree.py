# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  # Both nodes are None
            return True
        if p and q and p.val == q.val:  # Both nodes exist and have the same value
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False  # One of the nodes is None or their values differ
