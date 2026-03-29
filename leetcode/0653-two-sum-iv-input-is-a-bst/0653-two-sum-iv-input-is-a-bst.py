# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(root,vals):
            if not root:
                return 0
            inorder(root.left,vals)
            vals.append(root.val)
            inorder(root.right,vals)
            return vals
        vals=[]
        inorder(root,vals)
        for i in range(len(vals)):
            for j in range(i+1,len(vals)):
                if vals[i]+vals[j]==k:
                    return True
        return False