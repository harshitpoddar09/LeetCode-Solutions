# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans=[]
        def inorder(root,ans):
            if not root:
                return
            inorder(root.left,ans)
            ans.append(root.val)
            inorder(root.right,ans)
        inorder(root,ans)
        new=TreeNode(ans[0])
        cur=new
        for i in range(1,len(ans)):
            cur.right=TreeNode(ans[i])
            cur=cur.right
        return new