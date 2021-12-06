# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans=0
        def paths(root,cur):
            if not root:
                return
            cur+=str(root.val)
            if not root.left and not root.right:
                self.ans+=int(cur)
                return 
            paths(root.left,cur)
            paths(root.right,cur)
            return
        paths(root,'')
        return self.ans