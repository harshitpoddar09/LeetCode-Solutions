#SUBMISSION 2 - Iterative 36ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if not root:
            return []
        level=[root]
        while level:
            ans.append([node.val for node in level])
            temp=[]
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level=temp
        return ans

#SUBMISSION 1 - using Recursion 128ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def height(root):
            if not root:
                return 0
            lheight=height(root.left)
            rheight=height(root.right)
            if lheight<rheight:
                return rheight+1
            return lheight+1
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
        result=[]
        for i in range(1,h+1):
            result.append(curLevel(root,i,[]))
        return result