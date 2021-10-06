# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def height(root):
            if not root:
                return 0
            lheight=height(root.left)
            rheight=height(root.right)
            if lheight>rheight:
                return lheight+1
            else:
                return rheight+1
        def curLevel(root,level,ans):
            if not root:
                return 
            if level==1:
                ans.append(root.val)
            elif level>1:
                curLevel(root.left,level-1,ans)
                curLevel(root.right,level-1,ans)
            return ans
        h=height(root)
        res=[]
        for i in range(h,0,-1):
            res.append(curLevel(root,i,[]))
        return res