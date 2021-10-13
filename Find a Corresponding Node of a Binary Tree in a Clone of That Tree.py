# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        level=[cloned]
        while level:
            temp=[]
            for node in level:
                if node.val==target.val:
                    return node
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level=temp