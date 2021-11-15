# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d={}
        def traverse(root):
            if not root:
                return 
            if root.val not in d:
                d[root.val]=0
            d[root.val]+=1
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        ans=[]
        cur=0
        for key in d:
            if d[key]>cur:
                ans=[key]
                cur=d[key]
            elif d[key]==cur:
                ans.append(key)
        return ans