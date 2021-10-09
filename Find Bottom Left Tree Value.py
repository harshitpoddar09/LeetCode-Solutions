# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        level=[root]
        left_view=[]
        while level:
            left_view.append(level[0])
            temp=[]
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level=temp
        return left_view[-1].val