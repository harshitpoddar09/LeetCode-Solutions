# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if not root:
                return
            nodes.add(root.val)
            traverse(root.left)
            traverse(root.right)
        nodes=set()
        traverse(root)
        nodes=sorted(nodes)
        if len(nodes)<2:
            return -1
        return nodes[1]