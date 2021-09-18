#Submission 2 - 64ms
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack=0
        ans=''
        for i in S:
            if i=='(':
                if stack:
                    ans+='('
                stack+=1
            else:
                if stack!=1:
                    ans+=')'
                stack-=1
        return ans

#Submission 1 - 40ms
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack=[]
        ans=''
        for i in S:
            if i=='(':
                if stack:
                    ans+='('
                stack.append(')')
            else:
                if len(stack)!=1:
                    ans+=')'
                stack.pop()
        return ans