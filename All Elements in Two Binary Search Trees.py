# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root,ans):
            if not root:
                return
            inorder(root.left,ans)
            ans.append(root.val)
            inorder(root.right,ans)
        tree1=[]
        inorder(root1,tree1)
        tree2=[]
        inorder(root2,tree2)
        return sorted(tree1+tree2)