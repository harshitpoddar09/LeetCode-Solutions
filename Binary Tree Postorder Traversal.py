# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        def postorder(root,ans):
            if not root:
                return
            postorder(root.left,ans)
            postorder(root.right,ans)
            ans.append(root.val)
            return ans
        return postorder(root,ans)