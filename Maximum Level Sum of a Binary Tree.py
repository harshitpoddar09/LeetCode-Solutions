# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans=1
        cur_sum=-float('inf')
        max_sum=-float('inf')
        level=[root]
        lev=1
        while level:
            cur_sum=0
            temp=[]
            for node in level:
                cur_sum+=node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if cur_sum>max_sum:
                max_sum=cur_sum
                ans=lev
            level=temp
            lev+=1
        return ans