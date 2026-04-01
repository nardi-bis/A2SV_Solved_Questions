# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {i:x for x,i in enumerate(inorder)}
        self.preorder_idx = 0
        def rec(left, right):
            if left > right:
                return None
            root_val = preorder[self.preorder_idx]
            self.preorder_idx += 1

            root = TreeNode(root_val)
            mid = inorder_idx[root_val]


            root.left = rec(left, mid-1)
            root.right = rec(mid+1, right)

            return root
        return rec(0, len(preorder)-1)


        