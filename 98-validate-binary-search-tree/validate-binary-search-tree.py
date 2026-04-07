# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans_inorder = []
        def ino(n):
            if n == None:
                return 
            ino(n.left)
            ans_inorder.append(n.val)
            ino(n.right)
        ino(root)

        x = set(ans_inorder)
        if len(x) != len(ans_inorder):
            return False
            
        return ans_inorder == sorted(ans_inorder)
   
        
       


        