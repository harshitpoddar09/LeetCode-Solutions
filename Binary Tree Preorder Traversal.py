#SUBMISSION 2 - using Iteration 32ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        if not root:
            return
        stack=[root]
        while stack:
            q=stack.pop()
            ans.append(q.val)
            if q.right:
                stack.append(q.right)
            if q.left:
                stack.append(q.left)
        return ans

#SUBMISSION 1 - using Recursion 24ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        def preorder(root,ans):
            if not root:
                return
            ans.append(root.val)
            preorder(root.left,ans)
            preorder(root.right,ans)
            return ans
        return preorder(root,ans)