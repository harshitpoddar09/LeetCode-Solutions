# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        global ans
        ans=0
        def valsum(root):
            global ans
            if not root:
                return 0
            leftsum=valsum(root.left)
            rightsum=valsum(root.right)
            tilt=abs(leftsum-rightsum)
            ans+=tilt
            return root.val+leftsum+rightsum
        valsum(root)
        return ans