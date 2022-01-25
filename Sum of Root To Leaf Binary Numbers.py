#SUBMISSION 2 - 44ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def traverse(root,cur):
            if root.left:
                traverse(root.left,2*cur+root.val)
            if root.right:
                traverse(root.right,2*cur+root.val)
            if not root.left and not root.right:
                cur=2*cur+root.val
                self.ans+=cur
                return
        traverse(root,0)
        return self.ans

#SUBMISSION 1 - 72ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def traverse(root,cur):
            if root.left:
                traverse(root.left,cur+str(root.val))
            if root.right:
                traverse(root.right,cur+str(root.val))
            if not root.left and not root.right:
                cur+=str(root.val)
                self.ans+=int(cur,2)
                return
        traverse(root,'')
        return self.ans