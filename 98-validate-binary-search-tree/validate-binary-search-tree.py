# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(node):
            mels = [True, node.val, node.val]
            if node.left:
                lt, lmn, lmx = bst(node.left)
                mels[0] = mels[0] and lt
                mels[1] = min(mels[1], lmn)
                mels[2] = max(mels[2], lmx)
                mels[0] = mels[0] and (node.val > lmx)
            if node.right:
                rt, rmn, rmx = bst(node.right)
                mels[0] = mels[0] and rt
                mels[1] = min(mels[1], rmn)
                mels[2] = max(mels[2], rmx)
                mels[0] = mels[0] and (node.val < rmn)
            return mels
        return bst(root)[0]

            


        