#SUBMISSION 2 - 141ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        if not root:
            return
        root.val=0
        level=[root]
        self.nodes=set()
        while level:
            temp=[]
            for node in level:
                self.nodes.add(node.val)
                if node.left:
                    node.left.val=(2*node.val)+1
                    temp.append(node.left)
                if node.right:
                    node.right.val=(2*node.val)+2
                    temp.append(node.right)
            level=temp

    def find(self, target: int) -> bool:
        return target in self.nodes


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

#SUBMISSION 1 - 684ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        if not root:
            return
        root.val=0
        level=[root]
        self.nodes=[]
        while level:
            temp=[]
            for node in level:
                self.nodes.append(node.val)
                if node.left:
                    node.left.val=(2*node.val)+1
                    temp.append(node.left)
                if node.right:
                    node.right.val=(2*node.val)+2
                    temp.append(node.right)
            level=temp

    def find(self, target: int) -> bool:
        return target in self.nodes


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)