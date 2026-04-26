# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #ps = previous sum 
        #cs = current sum
        def dfs(root, ps):
            if not root:
                return
            cs = ps + root.val
            x = cs - targetSum
            if x in freq:
                self.count += freq[x]
            if cs in freq:
                freq[cs] += 1
            else:
                freq[cs] = 1
            dfs(root.left, cs)
            dfs(root.right, cs)
            freq[cs] -= 1
        self.count = 0
        freq = {0:1} # frequency for the path that checks 
        dfs(root, 0) # root, previous one
        return self.count

        