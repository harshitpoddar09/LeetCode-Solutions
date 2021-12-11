#SUBMISSION 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root,key):
            if root is None:
                return root
            if key<root.val:
                root.left=delete(root.left,key)
            elif key>root.val:
                root.right=delete(root.right,key)
            else:
                if root.left is None and root.right is None:
                    return None
                elif root.left is None:
                    temp=root.right
                    root=None
                    return temp
                elif root.right is None:
                    temp=root.left
                    root=None
                    return temp
                parent=root
                suc=root.right
                while suc.left is not None:
                    parent=suc
                    suc=suc.left
                if parent!=root:
                    parent.left=suc.right
                else:
                    parent.right=suc.right
                root.val=suc.val
            return root
        return delete(root,key)

#SUBMISSION 1 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minimumVal(node):
            cur=node
            while cur.left is not None:
                cur=cur.left
            return cur
        def delete(root,key):
            if root is None:
                return root
            if key<root.val:
                root.left=delete(root.left,key)
            elif key>root.val:
                root.right=delete(root.right,key)
            else:
                if root.left is None:
                    temp=root.right
                    root=None
                    return temp
                elif root.right is None:
                    temp=root.left
                    root=None
                    return temp
                temp=minimumVal(root.right)
                root.val=temp.val
                root.right=delete(root.right,temp.val)
            return root
        return delete(root,key)