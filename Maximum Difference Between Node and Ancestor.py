# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def diff(node,maxi,mini):
            if not node:
                return maxi-mini
            maxi=max(maxi,node.val)
            mini=min(mini,node.val)
            left=diff(node.left,maxi,mini)
            right=diff(node.right,maxi,mini)
            return max(left,right)
        return diff(root,root.val,root.val)