#SUBMISSION 2 - 183ms 15.4mb
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val!=root2.val:
                return False
            return isIdentical(root1.left,root2.left) and isIdentical(root1.right,root2.right)
        if isIdentical(root,subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

#SUBMISSION 1 - 183ms 14.6mb
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val!=root2.val:
                return False
            return isIdentical(root1.left,root2.left) and isIdentical(root1.right,root2.right)
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        level=[root]
        while level:
            for node in level:
                if node.val==subRoot.val:
                    if isIdentical(node,subRoot):
                        return True
            temp=[]
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level=temp
        return False