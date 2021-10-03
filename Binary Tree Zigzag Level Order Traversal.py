# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def height(root):
            if not root:
                return 0
            lheight=height(root.left)
            rheight=height(root.right)
            if lheight>rheight:
                return lheight+1
            else:
                return rheight+1
        def curLevel(root,level,flag,ans):
            if not root:
                return
            if level==1:
                ans.append(root.val)
            elif level>1:
                if flag:
                    curLevel(root.left,level-1,flag,ans)
                    curLevel(root.right,level-1,flag,ans)
                else:
                    curLevel(root.right,level-1,flag,ans)
                    curLevel(root.left,level-1,flag,ans)
            return ans
        h=height(root)
        res=[]
        flag=True
        for i in range(1,h+1):
            res.append(curLevel(root,i,flag,[]))
            flag=not flag
        return res