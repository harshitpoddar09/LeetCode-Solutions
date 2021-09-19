#Submission 2 - 28ms
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left=0
        right=0
        for i in s:
            if i=='(':
                left+=1
            else:
                if left:
                    left-=1
                else:
                    right+=1
        return left+right

#Submission 1 - 60ms
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        ans=0
        for i in s:
            if i=='(':
                stack.append(')')
            else:
                if stack and i==stack[-1]:
                    stack.pop()
                else:
                    ans+=1
        return ans+len(stack)