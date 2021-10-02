#SUBMISSION 2 - using Stack 28ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        stack=[]
        while 1:
            if root:
                stack.append(root)
                root=root.left
            elif stack:
                root=stack.pop()
                ans.append(root.val)
                root=root.right
            else:
                break
        return ans

#SUBMISSION 1 - using Recursion 28ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        def inorder(root,ans):
            if not root:
                return 
            inorder(root.left,ans)
            ans.append(root.val)
            inorder(root.right,ans)
            return ans
        return inorder(root,ans)