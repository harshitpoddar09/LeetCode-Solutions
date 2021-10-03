# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        lheight=self.maxDepth(root.left)
        rheight=self.maxDepth(root.right)
        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1