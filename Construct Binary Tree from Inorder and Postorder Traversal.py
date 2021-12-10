# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d={}
        for i in range(len(inorder)):
            d[inorder[i]]=i
        n=len(postorder)-1
        global idx
        idx=n
        def convert(inorder,postorder,start,end):
            global idx
            if start>end:
                return
            val=postorder[idx]
            node=TreeNode(val)
            idx-=1
            if start==end:
                return node
            i=d[val]
            node.right=convert(inorder,postorder,i+1,end)
            node.left=convert(inorder,postorder,start,i-1)
            return node
        return convert(inorder,postorder,0,n)