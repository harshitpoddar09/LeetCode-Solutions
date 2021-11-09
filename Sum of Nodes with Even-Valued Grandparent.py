# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        cur=0
        if root.val%2==0:
            if root.left:
                if root.left.left:
                    cur+=root.left.left.val
                if root.left.right:
                    cur+=root.left.right.val
            if root.right:
                if root.right.left:
                    cur+=root.right.left.val
                if root.right.right:
                    cur+=root.right.right.val
        return self.sumEvenGrandparent(root.left)+self.sumEvenGrandparent(root.right)+cur